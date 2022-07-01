from django.conf.urls import url, include
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Pastebin API')

schema_view = get_schema_view(
    openapi.Info(
        title="Data Mining services API",
        default_version='v1',
        description="This project provids some services for data cleaning process in data mining",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mostafanazary90@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',cache_timeout=0), name='schema-redoc'),
    # url(r'^$', schema_view),
    url('service1/', include('service1.urls')),
    url('service2/', include('service2.urls')),
    # url(r'^api/v1/service3', include('service3.urls')),
    # url(r'^api/v1/service4', include('service4.urls'))
]
