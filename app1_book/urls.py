from django.urls import path,re_path
from . import views
urlpatterns = [
    path('number',views.Take_num),
    path('send',views.send_file),
    path('watch',views.watch),
    path('audio',views.Audio_store),
    path('audio1',views.Audio_get),
    re_path('^$', views.Take_num),
]