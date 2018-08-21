import json

from G import ContentType

my_json = {"data":
    [
        {
            "type": ContentType.JSON,
            "values": "1"
        },
        {
            "type": ContentType.FORM_DATA,
            "values": "2"
        },
        {
            "type": ContentType.XML,
            "values": "3"
        },
        {
            "type": ContentType.MULTI_DATA,
            "values": "4"
        }
    ]
}

print(json.dumps(my_json, ensure_ascii=False))

print(type(my_json))

# print(my_json.get("data")[1].get('type') == 1)
