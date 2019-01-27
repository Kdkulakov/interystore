from django.urls import path, re_path, include
from authapp.views import user_login, user_logout, user_register, user_update, verify

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', user_login, name='login'),
    re_path(r'^logout/$', user_logout, name='logout'),
    re_path(r'^register/$', user_register, name='register'),
    re_path(r'^edit/$', user_update, name='update'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', verify, name='verify')

]
