import pandas as pd


def linear_interpolation(data, config):
    data = data.set_index('time')

    if config['time'] == 'daily':
        data = data.resample('D')

    elif config['time'] == 'monthly':
        data = data.resample('MS')

    elif config['time'] == 'hourly':
        data = data.resample('H')

    elif config['time'] == 'minutely':
        data = data.resample('T')

    else:
        data = None

    if data:
        data = data.ffill(1)
        if config['skip_holiday'] and config['time'] in ['daily', 'hourly', 'minutely']:
            data = data[~(pd.to_datetime(data.index).dayofweek.isin([3, 4]))]
        data = data.interpolate(method=config['interpolation'], order=config['interpolation_order'])
        data = data.reset_index()

    return data
