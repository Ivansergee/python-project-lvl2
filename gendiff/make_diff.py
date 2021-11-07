from parser import parse
import json


def make_diff(data1, data2):

    keys = {*data1, *data2}
    diff_list = []

    for key in keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff_list.append({
                    'name': key,
                    'prefix': None,
                    'children': make_diff(data1[key], data2[key])
                    })
            elif data1[key] == data2[key]:
                diff_list.append({
                    'name': key,
                    'value': data1[key],
                    'prefix': None
                    })
            else:
                diff_list.extend([
                    {
                        'name': key,
                        'value': data1[key],
                        'prefix': '-'
                    },
                    {
                        'name': key,
                        'value': data2[key],
                        'prefix': '+'
                    }
                    ])
        elif key in data1:
            diff_list.append({
                'name': key,
                'value': data1[key],
                'prefix': '-'
            })
        else:
            diff_list.append({
                'name': key,
                'value': data2[key],
                'prefix': '+'
            })
    return diff_list


d2 = '''{
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}'''

d1 = '''{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": true,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}'''

d3 = '''{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}'''

d4 = '''{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}'''

d5 = '''{
  "baz": 24,
  "common": {
    "setting1": "foo",
    "setting2": "bar"
  }
}'''

d6 = '''{
  "biz": 25,
  "common": {
    "setting1": "foo",
    "setting2": "bar",
    "setting3": {
        "inner": 24
    }
  }
}'''



d1, d2 = json.loads(d1), json.loads(d2)
d3, d4 = json.loads(d3), json.loads(d4)
d5, d6 = json.loads(d5), json.loads(d6)