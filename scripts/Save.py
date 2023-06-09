import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts"))
from scripts.Logger import Logger

import json
from typing import List, Tuple

class Save():
    """
        saves and loads checkpoints and prompts in a JSON
    """

    def __init__(self):
        self.file_name = "batchCheckpointPromptValues.json"
        self.logger = Logger()
        self.logger.debug = False

    def read_file(self):
        try:
            with open(self.file_name, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            return {"None": ("", "")}

    def store_values(self, name: str, checkpoints: str, prompts: str) -> None:
        data = {}

        # If the JSON file already exists, load the data into the dictionary
        if os.path.exists(self.file_name):
            data = self.read_file()

        # Check if the name already exists in the data dictionary
        if name in data:
            self.logger.log_info("Name already exists")
            return

        # Add the data to the dictionary
        data[name] = (checkpoints, prompts)

        # Append the new data to the JSON file
        with open(self.file_name, 'w') as f:
            json.dump(data, f)

        self.logger.log_info("saved checkpoints and Prompts")

    def read_value(self, name: str) -> Tuple[str, str]:
        name = name[0]
        data = {}

        if os.path.exists(self.file_name):
            data = self.read_file()
        else:
            raise RuntimeError("no save file found")

        x, y = tuple(data[name])
        self.logger.log_info("loaded save")

        return x, y

    def get_keys(self) -> List[str]:
        data = self.read_file()
        return list(data.keys())
