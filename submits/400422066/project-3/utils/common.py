import gzip
from flask import make_response, json
import pandas as pd
import numpy as np
import json
from khayyam import JalaliDate, JalaliDatetime
from dateutil import parser

def response_message(data=None, status=200):
    if status in range(200, 400):
        content = gzip.compress(json.dumps(data, ensure_ascii=False, indent=3, default=convert,
                                           sort_keys=False).encode('utf8'), 5)
    else:
        content = gzip.compress(
            json.dumps({'message': data, 'status': 'error'}, ensure_ascii=False, indent=3).encode('utf-8'), 5)
    response = make_response(content, status)
    response.headers['Content-length'] = len(content)
    response.headers['Content-Encoding'] = 'gzip'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


def convert(o):
    if isinstance(o, np.int64):
        return int(o)
    if isinstance(o, np.bool_):
        if o:
            return True
        else:
            return False
    if pd.isna(o):
        return None


def read_json_time_series(dict_data,config):
    j_data = json.dumps(dict_data)
    data = pd.read_json(j_data)
    #data.time = pd.to_datetime(data.time, unit='ms')

    if config['type'] == 'miladi':
        #data.time=data.time.apply(lambda x: parser.parse(x))
        data.time = pd.to_datetime(data.time, yearfirst=True)
    
    if config['type'] == 'shamsi':
        data.time=data.time.str.split("-")
        data.time=data.time.apply(lambda x: JalaliDate(int(x[0]),int(x[1]),int(x[2])).todate())
        data.time = pd.to_datetime(data.time, yearfirst=True)

    return data

def read_json_time_series_2(dict_data,config):
    j_data = json.dumps(dict_data)
    data = pd.read_json(j_data)
    data.time = pd.to_datetime(data.time, yearfirst=True)
   
    return data
