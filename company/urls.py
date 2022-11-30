from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^GET_LOGO_COMPANY/$',GET_LOGO_COMPANY,name="GET_LOGO_COMPANY"),
]