from django.conf.urls import url
from .views import *


urlpatterns = [
    url('', Interpolation.as_view(), name="interpolation"),
]
