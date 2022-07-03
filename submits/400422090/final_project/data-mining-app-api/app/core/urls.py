from django.urls import path

from core import views


app_name = 'core'

urlpatterns = [
    path('interpolation/', views.InterpolationView.as_view(), name='interpolation'),
    path('jalali-interpolation/', views.JalaliInterpolationView.as_view(), name='jalali-interpolation'),
    path('outlier-detection/', views.OutlierDetectionView.as_view(), name='outlier-detection'),
    path('imbalanced-classification/', views.ImbalancedClassificationView.as_view(), name='imbalanced-classification')
]
