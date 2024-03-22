import os
import json
from os.path import dirname, join


class Handler_api:

        def read_config_data(self, file="Otaku_api.json"):
            here = dirname(__file__)
            filename = join(here, file)
            with open(filename, 'r') as file:
               config = json.load(file)
               return config