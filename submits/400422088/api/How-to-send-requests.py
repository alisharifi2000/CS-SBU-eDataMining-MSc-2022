#how to send Requests
import requests, json

#define Url
api = "https://preprocessing-api-service.herokuapp.com/"
interpolate = api + "/interpolate"
outlier = api + "/outlier"
manage = api + "/management"

localhost = "http://127.0.0.1:80"
localhost_interpolate = localhost + "/interpolate"
localhost_outlier = localhost + "/outlier"
localhost_management = localhost + "/management"

#define Data
interpolate_data = open('./input_outputs/interpolate_data/input.json', 'r')
interpolate_data = json.load(interpolate_data)
outlier_data = open('./input_outputs/outlier_data/input.json', 'r')
outlier_data = json.load(outlier_data)
management_data = open('./input_outputs/management_data/input.json', 'r')
management_data = json.load(management_data)

#send Request
result=requests.post(url=outlier, json=outlier_data)

#convert to Json
result=result.json()

print("result:\n", result)