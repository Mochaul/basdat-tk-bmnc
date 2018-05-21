from django.conf.urls import url
from .views import login, register, register_user, authenticate_user

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^login/authenticate/$', authenticate_user, name='authenticate-user'),
    url(r'^register/$', register, name='register'),
    url(r'^register/register-user/$', register_user, name='register-user'),
]
