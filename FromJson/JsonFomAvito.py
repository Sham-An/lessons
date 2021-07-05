import json

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
data = json.loads(str_json)
print(data)
