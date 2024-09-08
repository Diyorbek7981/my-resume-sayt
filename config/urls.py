from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.static import serve

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resumeapp.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

