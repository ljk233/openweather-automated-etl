"""src.shared"""

import datetime as dt
import json
import os
from typing import Any

import yaml


def read_yaml(fp: str) -> dict[str, Any]:
    """ """
    with open(fp, "r") as f:
        return yaml.safe_load(f)


def setup_data_storage(
    storage_path: str = "./data", format_str: str = "%Y%m%d%H%M%S"
) -> str:
    """ """
    if not os.path.exists(storage_path):
        raise FileNotFoundError()

    # Construct the destination directoy name
    dest_dir_name = dt.datetime.now().strftime(format_str)

    # Construct the destination director path
    dest_dir_path = os.path.join(storage_path, dest_dir_name)

    # Create the destination directory
    if os.path.exists(dest_dir_path):
        raise FileExistsError()

    os.mkdir(dest_dir_path)

    return dest_dir_path


def write_to_json(data: dict[str, Any], fp: str) -> str:
    """ """
    with open(fp, "w") as f:
        json.dump(data, f, indent=2)
