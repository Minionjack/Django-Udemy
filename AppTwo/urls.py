from django.urls import re_path as url
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    url(r'^registrations/$', views.register, name='registrations'),
    url(r'^user_login/$', views.user_login, name='user_login')
    
]
