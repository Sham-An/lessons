import datetime
import urllib.parse
from logging import getLogger

import bs4
import requests
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from aparser.constants import STATUS_NEW
from aparser.constants import STATUS_READY
from aparser.models import Product
from aparser.models import Task


logger = getLogger(__name__)


class AvitoParser:
    PAGE_LIMIT = 10

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }
        self.task = None

    def find_task(self):
        obj = Task.objects.filter(status=STATUS_NEW).first()
        if not obj:
            raise CommandError('no tasks found')
        self.task = obj
        logger.info(f'Работаем над заданием {self.task}')

    def finish_task(self):
        self.task.status = STATUS_READY
        self.task.save()
        logger.info(f'Завершили задание')

    def get_page(self, page: int = None):
        params = {
            'radius': 0,
            'user': 1,
        }
        if page and page > 1:
            params['p'] = page

        url = self.task.url
        r = self.session.get(url, params=params)
        r.raise_for_status()
        return r.text

    @staticmethod
    def parse_date(item: str):
        logger.debug('parse_date: %s', item)
        params = item.strip().split(' ')
        if len(params) == 2:
            day, time = params
            if day == 'Сегодня':
                date = datetime.date.today()
            elif day == 'Вчера':
                date = datetime.date.today() - datetime.timedelta(days=1)
            else:
                logger.error('Не смогли разобрать день: %s', item)
                return

            time = datetime.datetime.strptime(time, '%H:%M').time()
            return datetime.datetime.combine(date=date, time=time)

        elif len(params) == 3:
            day, month_hru, time = params
            day = int(day)
            months_map = {
                'января': 1,
                'февраля': 2,
                'марта': 3,
                'апреля': 4,
                'мая': 5,
                'июня': 6,
                'июля': 7,
                'августа': 8,
                'сентября': 9,
                'октября': 10,
                'ноября': 11,
                'декабря': 12,
            }
            month = months_map.get(month_hru)
            if not month:
                logger.error('Не смогли разобрать месяц: %s', item)
                return

            try:
                today = datetime.datetime.today()
                time = datetime.datetime.strptime(time, '%H:%M')
                return datetime.datetime(day=day, month=month, year=today.year, hour=time.hour, minute=time.minute)
            except ValueError:
                year = datetime.datetime.strptime(time, '%Y')
                return datetime.datetime(day=day, month=month, year=year.year)

        else:
            logger.error('Не смогли разобрать формат:', item)
            return

    def parse_block(self, item):
        # Выбрать блок со ссылкой
        url_block = item.select_one('a.snippet-link')
        if not url_block:
            raise CommandError('bad "url_block" css')

        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        # Выбрать блок с названием
        title = url_block.string.strip()
        if not title:
            raise CommandError(f'no title for item: {url_block}')

        # Выбрать блок с названием и валютой
        price_block = item.select_one('span.price')
        if not price_block:
            raise CommandError('bad "price_block" css')

        price_block = price_block.get_text('\n')
        price_block = list(filter(None, map(lambda i: i.strip(), price_block.split('\n'))))
        if len(price_block) == 2:
            price, currency = price_block
            price = int(price.replace(' ', ''))
        elif len(price_block) == 1:
            # Бесплатно
            price, currency = 0, None
        else:
            price, currency = None, None
            logger.error(f'Что-то пошло не так при поиске цены: {price_block}, {url}')

        # Выбрать блок с датой размещения объявления
        date = None
        date_block = item.select_one('div.item-date div.js-item-date.c-2')
        if not date_block:
            raise CommandError('bad "date_block" css')

        absolute_date = date_block.get('data-absolute-date')
        if absolute_date:
            date = self.parse_date(item=absolute_date)

        try:
            p = Product.objects.get(url=url)
            p.task = self.task
            p.title = title
            p.price = price
            p.currency = currency
            p.save()
        except Product.DoesNotExist:
            p = Product(
                task=self.task,
                url=url,
                title=title,
                price=price,
                currency=currency,
                published_date=date,
            ).save()

        logger.debug(f'product {p}')

    def get_pagination_limit(self):
        text = self.get_page()
        soup = bs4.BeautifulSoup(text, 'lxml')

        container = soup.select('a.pagination-page')
        if not container:
            return 1
        last_button = container[-1]
        href = last_button.get('href')
        if not href:
            return 1

        r = urllib.parse.urlparse(href)
        params = urllib.parse.parse_qs(r.query)
        return min(int(params['p'][0]), self.PAGE_LIMIT)

    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')

        # Запрос CSS-селектора, состоящего из множества классов, производится через select
        container = soup.select('div.item.item_table.clearfix.js-catalog-item-enum.item-with-contact.js-item-extended')
        for item in container:
            self.parse_block(item=item)

    def parse_all(self):
        # Выбрать какое-нибудь задание
        self.find_task()

        limit = self.get_pagination_limit()
        logger.info(f'Всего страниц: {limit}')

        for i in range(1, limit + 1):
            logger.info(f'Работаем над страницей {i}')
            self.get_blocks(page=i)

        # Завершить задание
        self.finish_task()


class Command(BaseCommand):
    help = 'Парсинг Avito'

    def handle(self, *args, **options):
        p = AvitoParser()
        p.parse_all()
