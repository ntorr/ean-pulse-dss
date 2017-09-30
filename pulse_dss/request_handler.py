import json
import pandas as pd
from flask import abort


def validate_request_data(request):
    if not request.data:
        abort(400)
    data_dict = json.loads(request.data)
    fields = list(data_dict)
    if 'train' not in fields and 'score' not in fields and 'notebook' not in fields:
        abort(400)
    return data_dict


def convert_dict_to_df(args):
    return pd.read_json(json.dumps(args), orient='split')


def convert_df_to_json(df):
    return df.to_json(orient='split')
