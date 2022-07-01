from khayyam import JalaliDate

def convert_shamsi_to_miladi(data):
    for index, time in data['time'].items():
        year, month, day = time.split('-')
        data['time'][index] = JalaliDate(year, month, day).todate()
    return data


def convert_miladi_to_shamsi(data):
    for index, time in data['data']['time'].items():
        data['data']['time'][index] = str(JalaliDate(time))
    return data


def response_data(data, config):
    if config['type'] == "shamsi":
        data = convert_miladi_to_shamsi(data)
    return data

