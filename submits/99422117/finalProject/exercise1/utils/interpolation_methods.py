def linear_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data


def spline_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'], order=2)
        data.reset_index(inplace=True)

    else:
        data = None

    return data


def pad_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data


def nearest_interpolation(data, config):
    if config['time'] == 'monthly':
        data = data.set_index('time')
        data = data.resample('M')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'daily':
        data = data.set_index('time')
        data = data.resample('D')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'hourly':
        data = data.set_index('time')
        data = data.resample('60T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    elif config['time'] == 'minutely':
        data = data.set_index('time')
        data = data.resample('T')
        data = data.interpolate(method=config['interpolation'])
        data.reset_index(inplace=True)

    else:
        data = None

    return data