from khayyam import JalaliDatetime


def do_interpolation(data, config):
    error = ""
    data = data.set_index('time')

    if config['time'] == 'daily':
        data = data.resample('D').interpolate()
    if config['time'] == "monthly":
        data = data.resample('MS').mean().interpolate()
    if config['time'] == "hourly":
        data = data.resample('H').interpolate()

    if config['skip_holiday'] and config['time'] == "daily":
        for index, _ in data.iterrows():
            weekday = JalaliDatetime(index).weekday()
            if weekday in [6, 5]:
                data = data.drop(index)

    try:
        method = config['interpolation']
    except Exception:
        error = ("the interpolation method should be provided")
        return data, error

    if method == "linear":
        data = data.interpolate(method=method)
    elif method in ["polynomial", "spline"]:
        try:
            order = config['order']
        except Exception as e:
            error = ("order should be provided for non linear interpolation method")
            return data, error
        if method == "polynomial" and int(order) % 2 == 0:
            error = ("Odd order is not acceptable for polynomial interpolation")
            return data, error
        try:
            data = data.interpolate(method=method, order=order)
        except Exception as error:
            return data, error
    else:
        error = ("the interpolation method is not acceptable")

    data.reset_index(inplace=True)
    return data, error
