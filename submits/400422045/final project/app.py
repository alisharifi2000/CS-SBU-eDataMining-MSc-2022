import pandas as pd
from flask import Flask, request
from utils.common import response_message, read_json_time_series
from utils.interpolation_methods import linear_interpolation
from khayyam import *

from utils.management import manage_imbalance
from utils.outlier_methods import outlier_detection

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def isup():
    return response_message('API is active')


@app.route('/service1', methods=['GET', 'POST'])
def interpolation():
    req = request.get_json()
    data, config = read_json_time_series(req['data'], req['config'])

    if 'interpolation_order' not in config:
        config['interpolation_order'] = 1

    if 'interpolation' not in config:
        config['interpolation'] = 'linear'

    config['skip_holiday'] = False

    if data.time.dtype == 'int64':
        data.time = pd.to_datetime(data.time, unit='ms')
    else:
        if config['time'] == 'daily':
            if config['type'] == 'shamsi':
                data['time'] = data['time'].apply(
                    lambda x: JalaliDatetime(int(x.split(" ")[0].split("-")[0]), int(x.split(" ")[0].split("-")[1]),
                                             int(x.split(" ")[0].split("-")[2])).todate())
            config['date_format'] = '%Y-%m-%d'
            data.time = pd.to_datetime(data.time, format=config['date_format'])
        elif config['time'] == 'monthly':
            if config['type'] == 'shamsi':
                data['time'] = data['time'].apply(
                    lambda x: JalaliDatetime(int(x.split(" ")[0].split("-")[0]), int(x.split(" ")[0].split("-")[1])).todate())
            config['date_format'] = '%Y-%m'
            data.time = pd.to_datetime(data.time, format='%Y-%m')
        elif config['time'] == 'minutely':
            if config['type'] == 'shamsi':
                data['time'] = data['time'].apply(
                    lambda x: JalaliDatetime(int(x.split(" ")[0].split("-")[0]), int(x.split(" ")[0].split("-")[1]),
                                             int(x.split(" ")[0].split("-")[2]), int(x.split(" ")[1].split(":")[0]),
                                             int(x.split(" ")[1].split(":")[1])).todate())
            config['date_format'] = '%Y-%m-%d %H:%M'
            data.time = pd.to_datetime(data.time, format='%Y-%m-%d %H:%M')
        elif config['time'] == 'hourly':
            if config['type'] == 'shamsi':
                data['time'] = data['time'].apply(
                    lambda x: JalaliDatetime(int(x.split(" ")[0].split("-")[0]), int(x.split(" ")[0].split("-")[1]),
                                             int(x.split(" ")[0].split("-")[2]), int(x.split(" ")[1].split(":")[0])).todate())

            config['date_format'] = '%Y-%m-%d %H:%M'
            data.time = pd.to_datetime(data.time, format='%Y-%m-%d %H')

    result = linear_interpolation(data, config)

    if config['type'] == 'shamsi':
        if config['time'] == 'daily':
            result['time'] = result['time'].apply(
                lambda x: JalaliDatetime(x).__str__())
        elif config['time'] == 'monthly':
            result['time'] = result['time'].apply(
                lambda x: JalaliDatetime(x).__str__())
        elif config['time'] == 'minutely':
            result['time'] = result['time'].apply(
                lambda x: JalaliDatetime(x).__str__())
        elif config['time'] == 'hourly':
            result['time'] = result['time'].apply(
                lambda x: JalaliDatetime(x).__str__())
    else:
        result['time'] = result['time'].dt.strftime(config['date_format'])

    result = result.to_json()

    return response_message(dict({"data": result}))


@app.route('/service2', methods=['GET', 'POST'])
def interpolation_shamsi():
    req = request.get_json()
    data, config = read_json_time_series(req['data'], req['config'])

    if 'interpolation_order' not in config:
        config['interpolation_order'] = 1

    if 'interpolation' not in config:
        config['interpolation'] = 'linear'

    if 'skip_holidays' not in config:
        config['skip_holidays'] = False

    if data.time.dtype == 'int64':
        data.time = pd.to_datetime(data.time, unit='ms')
    else:
        if config['time'] == 'daily':
            config['date_format'] = '%Y-%m-%d'
        elif config['time'] == 'monthly':
            config['date_format'] = '%Y-%m'
        elif config['time'] == 'minutely':
            config['date_format'] = '%Y-%m-%d %H:%M'
        elif config['time'] == 'hourly':
            config['date_format'] = '%Y-%m-%d %H:%M'
        data.time = pd.to_datetime(data.time, format=config['date_format'])

    result = linear_interpolation(data, config)

    print(result)

    if config['time'] == 'daily':
        result['time'] = result['time'].apply(
            lambda x: JalaliDatetime(x).__str__())
    elif config['time'] == 'monthly':
        result['time'] = result['time'].apply(
            lambda x: JalaliDatetime(x).__str__())
    elif config['time'] == 'minutely':
        result['time'] = result['time'].apply(
            lambda x: JalaliDatetime(x).__str__())
    elif config['time'] == 'hourly':
        result['time'] = result['time'].apply(
            lambda x: JalaliDatetime(x).__str__())

    result = result.to_json()

    return response_message(dict({"data": result}))


@app.route('/service3', methods=['GET', 'POST'])
def outlier():
    req = request.get_json()
    if req['config']['time_series']:
        data, config = read_json_time_series(req['data'], req['config'])
    else:
        data = pd.DataFrame.from_dict(req['data'])
        config = req['config']

    result = outlier_detection(data, config)

    result = result.to_json()

    return response_message(dict({"data": result}))


@app.route('/service4', methods=['GET', 'POST'])
def management():
    req = request.get_json()
    data = req['data']
    config = req['config']
    try:
        result = manage_imbalance(data, config)
    except IndexError as e:
        if str(e) == 'Invalid method':
            return response_message(dict({"error": "Invalid method"}), 400)

    result = result.to_json()
    return response_message(dict({"data": result}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
