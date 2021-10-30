from pathlib import Path
import pytest

from gendiff.generate_diff import generate_diff


@pytest.fixture
def data():
    f1_json = Path().cwd() / 'tests' / 'fixtures' / 'sample1.json'
    f2_json = Path().cwd() / 'tests' / 'fixtures' / 'sample2.json'
    f1_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample1.yml'
    f2_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample2.yaml'    
    return f1_json, f2_json, f1_yaml, f2_yaml


def test_generate_diff(data):
    assert generate_diff(data[0], data[0]) == '{\n  follow: False\n  host: hexlet.io\n  proxy: 123.234.53.22\n  timeout: 50\n}'
    assert generate_diff(data[0], data[1]) == '{\n+ follow: False\n  host: hexlet.io\n+ proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}'
    
    assert generate_diff(data[2], data[2]) == '{\n  follow: False\n  host: hexlet.io\n  proxy: 123.234.53.22\n  timeout: 50\n}'
    assert generate_diff(data[2], data[3]) == '{\n+ follow: False\n  host: hexlet.io\n+ proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n}'