from flask import Flask, request
from utils.common import response_message, read_json_time_series , read_json_time_series_jalali , gregorian_jalali
from utils.interpolation_methods import linear_interpolation , spline_interpolation
import khayyam as kh
import numpy as np
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# swagger configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app name' : "Final Data Mining Services"
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET', 'POST'])
def isup():
    return response_message('API is active!!!')


@app.route('/service1', methods=['GET', 'POST'])
def interpolation1():
    req = request.get_json()
    config = req['config']
    
    if config['type'] == 'miladi':
        data = read_json_time_series(req['data'])
        
    elif config['type'] == 'shamsi' :
        data = read_json_time_series_jalali(req['data'])

    
    if config['interpolation'] == 'linear' :
        result = linear_interpolation(data, config)
    elif config['interpolation'] == 'spline' :
        result = spline_interpolation(data, config)

    if config['type'] == 'miladi':
        result.time = result.time.dt.strftime('%Y-%m-%d %H:%M:%S')
    elif config['type'] == 'shamsi' :
        result.time = result.time.apply(gregorian_jalali)
    
    result = result.to_json(date_format = 'iso')
    return response_message(dict({"data": result}))



@app.route('/service2', methods=['GET', 'POST'])
def interpolation2():
    req = request.get_json()
    config = req['config']

    
    data = read_json_time_series(req['data'])

    
    if config['interpolation'] == 'linear' :
        result = linear_interpolation(data, config)
    elif config['interpolation'] == 'spline' :
        result = spline_interpolation(data, config)

    result.time = result.time.apply(gregorian_jalali)
    
    result = result.to_json(date_format = 'iso')
    return response_message(dict({"data": result}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
