import json

from django.http import JsonResponse    
from rest_framework import generics

from utils.common import response_data
from utils.interpolation_methods import do_interpolation
from .utils import read_json_time_series
from .serializers import Service1Serializer


class Interpolation(generics.GenericAPIView):
    serializer_class = Service1Serializer

    def post(self, request):
        req = json.loads(request.body)
        config = req['config']
        data = req['data']
        data, error = read_json_time_series(data, config)
        if error:
            return JsonResponse(error, safe=False, status=400)
        data, error = do_interpolation(data, config)
        if error:
            return JsonResponse(error, safe=False, status=400)
        result = {'data': data.to_dict()}
        result = response_data(result, config)
        return JsonResponse(result, safe=False)