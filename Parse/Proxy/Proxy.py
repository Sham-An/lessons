import requests
from bs4 import BeautifulSoup
from random import choice
#from lxml import html

#https://youtu.be/MKq3u9NbpYE?t=1177
#https://youtu.be/MKq3u9NbpYE?t=2083
# Проксирование https://habr.com/ru/post/322608/
#Прокси листы https://hidemy.name/ru/proxy-list/
#https://free.proxy-sale.com/proxy-checker/
#https://www.ip-adress.com/proxy-list
from fake_useragent import UserAgent

def get_html(url, useragent=None, proxy=None):
    prox = 'http://31.31.76.37:80'
    print('Вход get_html ' + url+'  '+ useragent +' '+proxy)
    #r = requests.get(url)
    r = requests.get(url, headers=useragent, proxies=proxy)
    #r = requests.get(url, headers=useragent)
    print('Выход get_html ' + r.text)
    return r.text



def get_ip(html):
    print('Proxy & UsAg')
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = UserAgent().random
    print(ip)
    print(ua)
    print('________________________')


def main():
    #url_1 = 'https://www.avito.ru/rostov-na-donu/tovary_dlya_kompyutera?p=1&q=видеокарты'
    #url = 'http://sitespy.ru/my-ip' #https://youtu.be/MKq3u9NbpYE
    url = 'https://www.ip-adress.com/proxy-list'
    #useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies').read().split('\n')
    print(type(proxies), proxies)

    for proxy in proxies: #Проверяем и выбираем первый попавший рабочий прокси
        prox_elem={'http': 'http://'+proxy}
        print(prox_elem)
        r = requests.get(url, proxies=prox_elem)
        if r.status_code == requests.codes['ok']:
            print(r.text)
            print("ОК!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(type(r))
            break
        #print(response.text())
    #print('res = ', res)

    for i in range(10):
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = UserAgent().random
        print(proxy)
        print(useragent)
        try:
            html = get_html(url, useragent, proxy)
        except:
            continue
        #html = get_html(url, useragent, proxy)
        print('html = ' + html)
        get_ip(html)
        print('html = '+html)




if __name__ == '__main__':
    main()
