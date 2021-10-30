from gendiff.generate_diff import generate_diff
from pathlib import Path
import pytest


@pytest.fixture
def json_data():
    f1 = Path().cwd() / 'tests' / 'fixtures' / 'sample1.json'
    f2 = Path().cwd() / 'tests' / 'fixtures' / 'sample2.json'
    return f1, f2


def test_generate_diff(json_data):
    assert generate_diff(json_data[0], json_data[0]) == '{\n  follow: False\n  host: hexlet.io\n  proxy: 123.234.53.22\n  timeout: 50\n}'
    assert generate_diff(*json_data) == '{\n+ follow: False\n  host: hexlet.io\n+ proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}'