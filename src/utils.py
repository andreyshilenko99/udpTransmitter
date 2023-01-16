import json

import yaml


def from_json_to_list(file_name: str) -> list:
    with open(file_name) as f:
        data = json.load(f)
        return data['dump']


def get_config(file_name: str) -> dict:
    with open(file_name) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config
