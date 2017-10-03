import os
import json
import logging
import requests
import pandas as pd
logging.basicConfig(level='INFO')


# read data into python object
path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
data = json.load(open(os.path.join(path, 'example.json')))

# re-serialize as json
data_as_json = json.dumps(dict(data))

# log request data
logging.info('sending the following data as a request %s' % data_as_json)

# request score
r = requests.post('http://localhost:5000/score', data=data_as_json)

# json response
out = r.json()
logging.info(out)

out_json = json.dumps(out)

# convert result to DataFrame
df = pd.read_json(out_json, orient='split')
logging.info(df)
