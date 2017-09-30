import os
import json
import logging
import requests

logging.basicConfig(level='INFO')

base = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

data = json.load(open(os.path.join(base, 'example.json')))
logging.info(data)
data_as_json = json.dumps(dict(data))
logging.info(data_as_json)


r = requests.post('http://localhost:5000/score', data=data_as_json)

logging.info(r)
