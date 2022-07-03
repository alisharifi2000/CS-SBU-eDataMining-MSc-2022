from utils.common import read_json_time_series
import pandas as pd

def inter(data, time, method):
    if time == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
    elif time == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
    data = data.interpolate(method=method)
    data.reset_index(inplace=True)
    return data


def interpolation(data ,config):
    #change data format to pandas
    data = read_json_time_series(data)
    time = config['time'].lower()
    method = config['interpolation'].lower()
    data['time'] = pd.to_datetime(data['time'], unit='ms')
    #interpolation
    data = inter(data, time, method)
    #convert to json
    data = data.to_json()
    return data


