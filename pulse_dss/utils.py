import json
import pandas as pd
from flask import abort


def validate_request_data(request):
    if not request.data:
        abort(400)
    data_dict = json.loads(request.data)
    fields = list(data_dict)
    if 'train' not in fields and 'score' not in fields:
        abort(400)
    return data_dict


def convert_to_df(args):
    return pd.DataFrame(**args)
