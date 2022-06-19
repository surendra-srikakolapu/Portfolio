from django.urls import path
from . import views
from django.conf import settings
from django.urls import path, re_path
from .views import Files
from django.views.static import serve

urlpatterns = [
        path('', views.index, name="index"),
         path('file', Files, name='download-list'),
    re_path
    (r'download/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]
