import json


def callback(field, keyword):
    print(f'Callback: {field=}, {keyword=}')


def parse_json(json_str: str,
               keyword_callback,
               required_fields=None,
               keywords=None):
    if required_fields is None or keywords is None:
        return "Ничего не может быть найдено!"
    try:
        json_doc = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        return "Передана некорректная json-строка!"
    for field in required_fields:
        for word in keywords:
            try:
                if word in json_doc[field]:
                    keyword_callback(field, word)
            except KeyError:
                continue
    return None
