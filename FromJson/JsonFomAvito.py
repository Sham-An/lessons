#FROM https://www.youtube.com/watch?v=rIhygmw9HZM&t=301s
import json
import shutil
import sys



str_json = """
{
    "status": "ok",
    "data": [
        {
            "id": "621550",
            "name": "Крым"
        },
        {
            "id": "621590",
            "name": "Алтайский край"
        },
        {
            "id": "622470",
            "name": "Амурская область"
        },
        {
            "id": "622650",
            "name": "Архангельская область"
        },
        {
            "id": "662530",
            "name": "Ярославская область"
        },
        {
            "id": "662811",
            "name": "Республика Алтай"
        }
    ]
}
"""

print(type(str_json))


data = json.loads(str_json) #loadS из строки, load из файла
print(f"{data['status']} & {data['data']}")
#print(f"! = {data['status']} & {data['data']}")

for item in data['data']:
        print(f"{item['id']} = {item['name']}")

#Открываем файл
with open("avito_city.json", encoding='utf-8') as file: #Без указания кодировки выдает ошибку
#        print(file)

        data = json.load(file) #loadS из строки, load из файла
#        print(data)
#Поиск filter(lambda x: x['plate']=='E222EE177', str1['cars'])[0]['model']

for item in data['data']:
        print(f"Первый файл {item['id']} = {item['name']}")




#Записываем файл
with open("avito_city2.json",'w') as file:
        json.dump(data,file,indent=3) #indent добавляет структурированность с отступами =3

with open("avito_city2.json") as file:
        data = json.load(file)

for item in data['data']:
        print(f"Сохраненный {item['id']} = {item['name']}")

