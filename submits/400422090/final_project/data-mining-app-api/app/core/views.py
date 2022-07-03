from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from core.serializers import JSONFieldSerializer

from algorithms.interpolation import Interpolation
from algorithms.outlier_detection import OutlierDetection
from algorithms.imbalance_classification import ImbalancedClassification


schema_view = get_swagger_view(title='Data mining API')

urlpatterns = [
    url(r'^$', schema_view)
]


class BaseView(generics.CreateAPIView):
    """Base view for all 4 data mining services"""
    serializer_class = JSONFieldSerializer


class InterpolationView(BaseView):
    """
        Interpolate time series data including jalali(shamsi) time series and gregorian(miladi) time series

        JSON input structure: { 'data': ..., 'config': ... }

        Config containing type,time, and interpolation fields

        Supported type values are: 'miladi', 'shamsi'
        Supported time values are: 'daily', 'monthly', 'hourly', 'minutes', '5 minutes' or '5minutes' or 'five minutes'
        Supported interpolation values which is interpolation method are: 'linear' and 'spline'
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        try:
            dict_data_interpolated = Interpolation(serializer.data).interpolated_data
        except ValueError as e:
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(dict_data_interpolated, status=status.HTTP_200_OK, headers=headers)


class JalaliInterpolationView(BaseView):
    """
        Interpolate time series data including jalali(shamsi) time series and gregorian(miladi) time series

        JSON input structure: { 'data': ..., 'config': ... }

        Config containing type,time, interpolation, and skip_holiday fields

        Supported type values are: 'miladi', 'shamsi'
        Supported time values are: 'daily', 'monthly', 'hourly', 'minutes', '5 minutes' or '5minutes' or 'five minutes'
        Supported interpolation values which is interpolation method are: 'linear' and 'spline'
        Supported skip_holiday values which skips thursdays and fridays are: true, false (boolian)
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        # try:
        dict_data_interpolated = Interpolation(serializer.data, service_name='service2').interpolated_data
        # except ValueError as e:
        #     return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response(dict_data_interpolated, status=status.HTTP_200_OK, headers=headers)


class OutlierDetectionView(BaseView):
    """
        Find outlier data in dataset which can be time series or not

        JSON input structure: { 'data': ..., 'config': ... }
        Config containing time_series boolian which can be true or false

        Two methods implemented:
        method1: zscore > threshold(default=3) in normal distribution data

        method2: iqr distance from median
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        dict_data_outlier_detected = OutlierDetection(serializer.data).outlier_detected_data

        return Response(dict_data_outlier_detected, status=status.HTTP_200_OK, headers=headers)


class ImbalancedClassificationView(BaseView):
    """
        Balance imbalanced classification data using three methods:
        1- Under-sampling
        2- Over-sampling
        3- SMOTE

        JSON input structure: { 'data': ..., 'config': ... }

        Config containing method which can be: oversampling, undersampling, and SMOTE

        Major and minor class will be identified dynamically
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        try:
            dict_data_balanced = ImbalancedClassification(serializer.data).balanced_data
        except ValueError as e:
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)
        except AssertionError as e:
            return Response('method field is required', status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response(dict_data_balanced, status=status.HTTP_200_OK, headers=headers)

