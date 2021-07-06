from bs4 import BeautifulSoup


#https://youtu.be/7hn1_t2ZtJQ

#url=https://rest-app.net/api
#Категории
#//*[@id="wrapper"]/section/div/div/div[1]/div/div[3]/div[3]/div/div/div/table/tbody/tr[3] таблица категории (транспорт, недвижимость...)
#//*[@id="wrapper"]/section/div/div/div[1]/div/div[3]/div[3]/div/div/div/table/tbody//tr полная выборка элементов категории

#Регионы
#Регионы
#//*[@id="wrapper"]/section/div/div/div[1]/div/div[4]/div[3]/div/div/div/table/tbody/tr

#Группа Адыгея
#//*[@id="wrapper"]/section/div/div/div[1]/div/div[4]/div[3]/div/div/div/table/tbody/tr[1]/td[2]/div/div/label/text()
#Алтайский край
#//*[@id="wrapper"]/section/div/div/div[1]/div/div[4]/div[3]/div/div/div/table/tbody/tr[2]

# Get
#https://www.avito.ru/js/catalog?categoryId=10&locationId=652000&name=%D0%B4%D0%B2%D0%B8%D0%B3%D0%
# curl "https://www.avito.ru/js/catalog?categoryId=10&locationId=652000&name=^%^D0^%^B4^%^D0^%^B2^%^D0^%^B8^%^D0^%^B3^%^D0^%^B0^%^D1^%^82^%^D0^%^B5^%^D0^%^BB^%^D1^%^8C^%^20^%^D0^%^B2^%^D0^%^B0^%^D0^%^B7&geoCoords=47.222543^%^2C39.718732&cd=0&s=101&p=1&filterCategoryId=10&verticalCategoryId=0&rootCategoryId=1&countOnly=1" ^
#   -H "authority: www.avito.ru" ^
#   -H "accept: application/json" ^
#   -H "x-requested-with: XMLHttpRequest" ^
#   -H "x-source: client-browser" ^
#   -H "user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36" ^
#   -H "content-type: application/json" ^
#   -H "sec-fetch-site: same-origin" ^
#   -H "sec-fetch-mode: cors" ^
#   -H "sec-fetch-dest: empty" ^
#   -H "referer: https://www.avito.ru/rostov-na-donu/zapchasti_i_aksessuary?q=^%^D0^%^B4^%^D0^%^B2^%^D0^%^B8^%^D0^%^B3^%^D0^%^B0^%^D1^%^82^%^D0^%^B5^%^D0^%^BB^%^D1^%^8C+^%^D0^%^B2^%^D0^%^B0^%^D0^%^B7" ^
#   -H "accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7" ^
#   -H "cookie: u=2oklu8rg.8ml050.ahpe5zc5rv80; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; __cfduid=dd21b59929bed9e77d710aa96a6acae2c1613560069; _gcl_aw=GCL.1613560076.CjwKCAiAmrOBBhA0EiwArn3mfE74G4ZNVhrG6S8hqNrJT4qdqBuUr8ZmQMHD5gRgelHDZ8R_vrsdGBoCIqgQAvD_BwE; _gcl_au=1.1.1665627158.1613560076; av_last_utm_source=google; lastViewingTime=1613560077249; showedStoryIds=58-57-56-51-50-49-47-42-32; _ym_d=1613560078; _ym_uid=1613560077659463385; _ga=GA1.2.938067146.1613560077; _gac_UA-2546784-1=1.1613560079.CjwKCAiAmrOBBhA0EiwArn3mfE74G4ZNVhrG6S8hqNrJT4qdqBuUr8ZmQMHD5gRgelHDZ8R_vrsdGBoCIqgQAvD_BwE; __gads=ID=2b7154387e6e6118:T=1613560075:S=ALNI_MboAbZAYdteZepsJmF9bmbxj1qtjw; isCriteoSetNew=true; auth=1; sessid=e1a0312bcab3b811f2f3db2d67ae6c40.1613584957; _gid=GA1.2.1786652011.1613673994; buyer_selected_search_radius0=200; __utmz=99926606.1613770440.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none); _ym_isad=1; buyer_laas_location=621630; abp=1; no-ssr=1; f=5.367a37203faa7618a7d90a8d0f8c6e0b8a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d40477fde300814b1e85546b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264ed3de19da9ed218fe246b8ae4e81acb9fa51b1fde863bf5c12f8ee35c29834d631c9ba923b7b327da754f74ee9b0b17d2d06a78015522025902985db2d99140e2d15e264d035b0c55de9a27f1a0928bf4ab3440ca913fb1be94a4458c1a628f10fc772035eab81f5e146b8ae4e81acb9fa46b8ae4e81acb9faf5b8e78c6f0f62a3453eeb233e02b5e5586d1732f5123fe92da10fb74cac1eab2da10fb74cac1eab975fbcc148c02d7dc844364922ef6569a6ef565a9fc26059; v=1613901989; isLegalPerson=0; _ym_visorc=b; __utma=99926606.938067146.1613560077.1613770440.1613902037.2; __utmc=99926606; buyer_location_id=652000; luri=rostov-na-donu; buyer_popup_location=652000; SEARCH_HISTORY_IDS=0^%^2C4^%^2C; sx=H4sIAAAAAAACA1XQQZaCQAwE0Lv02kUaIhO8DUYIGrAdWwji8^%^2B4TF87TffpXdT1C0e6PzfTDv^%^2Bcqo7KgkWDSJGH3CHPYhf6eThn77tKjsSWWROQnmNVYGcMmtGEXq1jWJcSyem4CNf28nOd1VAHwF8YZJPv9m2zvo6muS7VXYI9kQxTxeEIApA^%^2BSyiKik4fbWizzlbe9Ioiqy5LQ8J^%^2Fs1qbjdbmdD1lFHBUjNCXIHi^%^2F2SRLGV8uY^%^2BvbUTMskA5N^%^2FDNGbCgu^%^2FyTHN22FprLhiNjIgL2kEfoZmht9kWTrZVFh3XMRpAiZSNEiW5GPLw1APrTTYrZoNnEzuJl^%^2FGjCjnL9KTnOxidZ9TPXTX1ziWmbNpZoU3uW3343C8FHbhnLyega^%^2FDDBlBhb62pDoWz^%^2BcfkXmv7vMBAAA^%^3D; so=1613902512; __utmb=99926606.4.9.1613902516940; buyer_from_page=catalog" ^
#   --compressed

