import json
import yaml


def from_json_to_list(file_name: str) -> list:
    f = open(file_name)
    data = json.load(f)
    f.close()
    return data['dump']


def get_config(file_name: str) -> dict:
    with open(file_name) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config
