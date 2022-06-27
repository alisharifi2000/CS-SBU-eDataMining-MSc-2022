from flask import Flask, request, render_template
import os
from utils.common import response_message
from utils.interpolation_methods import interpolation
from utils.outlier_detection_methods import outlier_detection
from utils.imbalance_management_methods import manage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def isup():
    return response_message('API is active')

@app.route('/api_docs')
def swagger():
    return render_template('index.html')

@app.route('/interpolate', methods=['GET', 'POST'])
def interpolate():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = interpolation(data, config)
    return response_message(dict({"data": result}))

@app.route('/outlier', methods=['GET', 'POST'])
def outlier():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = outlier_detection(data, config)
    return response_message(dict({"data": result}))

@app.route('/management', methods=['GET', 'POST'])
def management():
    req = request.get_json()
    data = req['data']
    config = req['config']
    result = manage(data, config)
    return response_message(dict({"data": result}))


port = os.environ.get("PORT", 5000)
if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=port)