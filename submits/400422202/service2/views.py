import json

from rest_framework import generics
from django.http import JsonResponse

from utils.common import response_data
from utils.interpolation_methods import do_interpolation

from .serializers import Service2Serializer
from .utils import read_json_time_series


class Interpolation(generics.GenericAPIView):
    serializer_class = Service2Serializer

    def post(self, request):
        req = json.loads(request.body)
        config = req['config']

        # This service should recive time in miladi (no input from user)
        config['type'] = "miladi"

        data = req['data']
        data, error = read_json_time_series(data, config)
        
        if error:
            return JsonResponse(error, safe=False, status=400)
        data, error = do_interpolation(data, config)

        if error:
            return JsonResponse(error, safe=False, status=400)
        result = {'data': data.to_dict()}

        # the time output of this service is shamsi
        config['type'] = "shamsi"

        result = response_data(result, config)
        return JsonResponse(result, safe=False)

