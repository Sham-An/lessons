#URL https://youtu.be/n6x1pzlRK8A
import time
import requests
import lxml.html
from bs4 import BeautifulSoup
import threading

#БЕЗ BeautifulSoup

# Debag part 2 переменные https://youtu.be/HpJYVIRuQbU
# Debag part 3 изменение брекпоинтов на принт https://youtu.be/QA_aGDIHakA
# Condition условие остановки если (переменная >= )
# Evaluate and log вывод в консоль строки формата f" текст {переменная}  "
#https://youtu.be/n6x1pzlRK8A?t=1784 (30:43)
class OlxParser:

    def __init__(self, base_url):
        self.base_url = base_url
        #self.last_time =

    def get_page(self):

        try:
            res = requests.get(self.base_url)
        except requests.ConnectionError:
            return


        if res.status_code < 400:
            return res.content

    def get_last_offer(self, html):
        html_tree = lxml.html.fromstring(html)
        #Из окна с таблицей элементов выбор элементов
        #AVITO дерево группы
        path = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div[2]//a[@itemprop="url"]'
        #path = './/div[@elementtiming="bx.catalog.container"]//div[@data-item-id and @id]'


        #www.olx.ua
        #path = './/table[@id="offers_table"]//td[@class="offer  "]'
        #path = './/table[@id="offers_table"]//td[@class="offer  "]'
        ###path = './/table[@id="offers_table"]//tr[@class="wrap"]'
        #path = './/table[@id="offers_table"]//tr[@class="wrap"]'
        #path = './/table[@id="offers_table"]//td[@class="offer promoted "]'


        #offers = html_tree.xpath('.//table[@id="offers_table"]//td[@class="offer promoted "]')
        #offers = html_tree.xpath('.//div[@elementtiming="bx.catalog.container"]//div[@data-item-id]//div//div//a')
        offers = html_tree.xpath(path)
 #############################################################
        #Пробуем BeautifulSoup
        soup = BeautifulSoup(html,features="lxml")
        #print(soup.prettify())
        for lnk in soup.find_all('a'):
            print("prn lnk ", lnk.get('href'))

        print("prn text ", soup.get_text())


##############################################################
        last_offer = str(offers[1]) #last_offer.text_content()
        #url_last=html_tree.xpath(path).get('href')

        url_last = str('https://www.avito.ru')+html_tree.xpath(path)[1].get('href')

        print(len(offers),html_tree, url_last) # offers)

        try:
            last_offer = html_tree.xpath(path)[1]
            #print(last_offer.text_content())#https://youtu.be/n6x1pzlRK8A?t=1763
            #link = last_offer.xpath('.//a')[1].get('href') #Берем из элемента last [1] второй элемент и получаем из него ссылку на описание
            #link = last_offer.xpath(path).get('href')  # Берем из элемента last [1] второй элемент и получаем из него ссылку на описание
            link = url_last

            #Забираем время объявления
            ##time_node = last_offer.xpath('.//table/tbody/tr[2]//p/text')[2]
            ##cur_time = time_node.strip()[-5:] #берем последние 5 символов и убираем пробелы
            #print(link)
        except (IndexError, AttributeError):
            return
        #
        # if self.last_time != cur_time:
        #     self.last_time = cur_time
        #     print(cur_time, link)

    def run(self): # https://youtu.be/n6x1pzlRK8A?t=2651
        while True:
            page = self.get_page()

            if page is None:
                time.sleep(1)
                continue

            self.get_last_offer(page)
            time.sleep(1)

if __name__=="__main__":

    #url_='https://www.olx.ua/list/'
    url = 'https://www.avito.ru/rostov-na-donu/zapchasti_i_aksessuary'
    #url='https://www.olx.ua/transport/'
    #url_2 = 'https://www.olx.ua/nedvizhimost/'
    parser = OlxParser(url)
    #parser_2 = OlxParser(url_2)
    parser.run() #выключил для многопоточности

    # https://youtu.be/n6x1pzlRK8A?t=3264 многопоточность
    #t1 = threading.Thread(target=parser.run)
    #t2 = threading.Thread(target=parser_2.run)


