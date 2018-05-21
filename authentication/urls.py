from django.conf.urls import url
from .views import login, register, register_user

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^register/register-user/$', register_user, name='register-user'),
]
