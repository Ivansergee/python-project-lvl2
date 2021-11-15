from gendiff import parse, make_diff, to_string, plain


def generate_diff(file1, file2, format='str'):
    if format == 'str':
        return to_string(make_diff(parse(file1), parse(file2)))
    elif format == 'plain':
        return plain(make_diff(parse(file1), parse(file2)))


d1 = '''{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
}'''

d2 = '''{
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
}'''

d3 = '''{
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

d4 = '''{
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
