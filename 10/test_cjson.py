import json
from unittest import TestCase

import ujson

import cjson


class TestCjson(TestCase):
    def test_success(self):
        json_str = '{"hello": 155, "world": "value", "example": "123"}'
        json_doc = json.loads(json_str)
        ujson_doc = ujson.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, cjson_doc)
        self.assertEqual(ujson_doc, cjson_doc)
        self.assertEqual(json_str, cjson.dumps(cjson.loads(json_str)))

    def test_loads_one_item(self):
        json_str = '{"world": "value"}'
        json_doc = json.loads(json_str)
        ujson_doc = ujson.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, cjson_doc)
        self.assertEqual(ujson_doc, cjson_doc)

    def test_loads_few_items(self):
        json_str = '{"hello": "word", "world": "513", "string": "empty"}'
        json_doc = json.loads(json_str)
        ujson_doc = ujson.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, cjson_doc)
        self.assertEqual(ujson_doc, cjson_doc)

    def test_loads_int_value(self):
        json_str = '{"hello": 123, "world": "513", "string": 251}'
        json_doc = json.loads(json_str)
        ujson_doc = ujson.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, cjson_doc)
        self.assertEqual(ujson_doc, cjson_doc)

    def test_dumps_one_item(self):
        obj = {"hello": "word"}
        json_str = json.dumps(obj)
        cjson_str = cjson.dumps(obj)
        self.assertEqual(json_str, cjson_str)

    def test_dumps_few_items(self):
        obj = {"hello": "word", "world": "513", "string": "empty"}
        json_str = json.dumps(obj)
        cjson_str = cjson.dumps(obj)
        self.assertEqual(json_str, cjson_str)

    def test_dumps_int_value(self):
        obj = {"hello": 123, "world": "513", "string": 251}
        json_str = json.dumps(obj)
        cjson_str = cjson.dumps(obj)
        self.assertEqual(json_str, cjson_str)
