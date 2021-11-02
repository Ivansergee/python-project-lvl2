import pytest
from pathlib import Path

from gendiff.parser import parse


@pytest.fixture
def data():
    f1_json = Path().cwd() / 'tests' / 'fixtures' / 'sample1.json'
    f1_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample1.yml'
    f2_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample2.yaml'    
    return f1_json, f1_yaml, f2_yaml


def test_parser(data, capfd):
    parse('wrong.txt')
    out, err = capfd.readouterr()
    assert out == 'wrong format\n'
    assert parse(data[0]) == {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": False}
    assert parse(data[1]) == {"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22", "follow": False}
    assert parse(data[2]) == {"timeout": 20, "verbose": True, "host": "hexlet.io"}