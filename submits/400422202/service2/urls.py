from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^', Interpolation.as_view(), name="interpolation"),
]
