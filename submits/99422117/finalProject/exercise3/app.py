from flask import Flask, request
from utils.common import response_message, read_json_time_series
from utils.outlierdetection_methods import zscorefilter, quantilefilter, iqrfilter
import pandas
import numpy


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def outlier_detection():
    req = request.get_json()
    data = read_json_time_series(req['data'])

    data['method1'] = zscorefilter(data.feature)
    data['method2'] = quantilefilter(data.feature)
    data['method3'] = iqrfilter(data.feature)

    json_result = data.to_json()
    return dict({"data": json_result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
