from flask import Flask, request
from utils.common import response_message, read_json_time_series, read_json_time_series_2
from utils.interpolation_methods import linear_interpolation
from utils.interpolation_methods import linear_interpolation_shamsi
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def isup():
    return response_message('API is active')






@app.route('/service1', methods=['GET', 'POST'])
def interpolation():
    req = request.get_json()
    config = req['config']
    data = read_json_time_series(req['data'],config)
    

    if config['type'] == 'miladi':
        result = linear_interpolation(data, config)
        result = result.to_json()
    
    if config['type'] == 'shamsi':
        result = linear_interpolation_shamsi(data, config)
        result = result.to_json(default_handler=str)
       
        
    return response_message(dict({"data": result}))



@app.route('/service2', methods=['GET', 'POST'])
def interpolation_2():
    req = request.get_json()
    config = req['config']
    data = read_json_time_series_2(req['data'],config)
    result = linear_interpolation_shamsi(data, config)
    result = result.to_json(default_handler=str)
        
    return response_message(dict({"data": result}))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
