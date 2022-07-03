def linear_interpolation(data, config):
    if config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        

    elif config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('MS').first()
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data


######
import numpy as np
import pandas as pd
from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime

def linear_interpolation_shamsi(data, config):
    if config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        data.time=data.time.apply(lambda x: JalaliDate(x))

    elif config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('MS').first()
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)
        data.time=data.time.apply(lambda x: JalaliDate(x))

    else:
        data = None

    return data
