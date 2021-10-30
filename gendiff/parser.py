import json
import yaml


def parse(file):
    path_str = str(file)
    if path_str.endswith('.json'):
        return json.load(open(file))
    elif path_str.endswith(('.yml', '.yaml')):
        return yaml.safe_load(open(file))
    else:
        return 'wrong format'
