import pandas as pd
from khayyam import JalaliDate

def linear_interpolation(data, config):
    if config['time'] == 'daily':
        print(type(data['time']))
        data['time'] = pd.to_datetime(data["time"], unit='ns')
        
        print(type(data['time']))
        data = data.set_index('time')
        

        
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data


def shamsi_linear_interpolation(data, config):
    if config['time'] == 'daily':
        data = data.set_index('time')
        print(data)
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
