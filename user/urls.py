from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Login/$',Login,name="Login"),
		url(r'^Register/$',Register,name="Register"),
]