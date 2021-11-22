from pathlib import Path
import pytest

from gendiff.generate_diff import generate_diff


@pytest.fixture
def data():
    f1_json = Path().cwd() / 'tests' / 'fixtures' / 'sample1.json'
    f2_json = Path().cwd() / 'tests' / 'fixtures' / 'sample2.json'
    f1_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample1.yml'
    f2_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample2.yaml'
    f1_nested_json = Path().cwd() / 'tests' / 'fixtures' / 'sample_nested1.json'
    f2_nested_json = Path().cwd() / 'tests' / 'fixtures' / 'sample_nested2.json'
    f1_nested_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample_nested1.yml'
    f2_nested_yaml = Path().cwd() / 'tests' / 'fixtures' / 'sample_nested2.yml'
    with open(Path().cwd() / 'tests' / 'fixtures' / 'expected' / 'exp_stylish.txt') as f, \
         open(Path().cwd() / 'tests' / 'fixtures' / 'expected' / 'exp_nested_stylish.txt') as g:
        expected = f.read()
        expected_nested = g.read()
    return {
        'json1': f1_json,
        'json2': f2_json,
        'yaml1': f1_yaml,
        'yaml2': f2_yaml,
        'json_nested1': f1_nested_json,
        'json_nested2': f2_nested_json,
        'yaml_nested1': f1_nested_yaml,
        'yaml_nested2': f2_nested_yaml,
        'expected': expected,
        'expected_nested': expected_nested
    }


def test_stylish(data):
    assert generate_diff(data['json1'], data['json2']) == data['expected']
    assert generate_diff(data['yaml1'], data['yaml2']) == data['expected']

    assert generate_diff(data['json_nested1'], data['json_nested2']) == data['expected_nested']
    assert generate_diff(data['yaml_nested1'], data['yaml_nested2']) == data['expected_nested']
