from django.urls import path
from .views import index, service_detail

urlpatterns = [
    path('', index, name='index'),
    path('service/<int:pk>/', service_detail, name='service-detail'),
]
