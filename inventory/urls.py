from django.conf.urls import url
from .views import *
from .query import *

urlpatterns=[
		url(r'^Save_Category/$',Save_Category,name="Save_Category"),
		url(r'^Save_SubCategory/$',Save_SubCategory,name="Save_SubCategory"),
		url(r'^GET_LIST_INVENTORY/$',GET_LIST_INVENTORY,name="GET_LIST_INVENTORY"),
		url(r'^GET_CATEGORY_MORE_SEARCHED/$',GET_CATEGORY_MORE_SEARCHED,name="GET_CATEGORY_MORE_SEARCHED"),
		url(r'^GET_LIST_SUBCATEGORIES/$',GET_LIST_SUBCATEGORIES,name="GET_LIST_SUBCATEGORIES"),
		url(r'^GET_ALL_CATEGORIES/$',GET_ALL_CATEGORIES,name="GET_ALL_CATEGORIES"),
		url(r'^LIST_PRODUCTS/$',LIST_PRODUCTS,name="LIST_PRODUCTS"),
		url(r'^GET_DETAIL_PRODUCT/$',GET_DETAIL_PRODUCT,name="GET_DETAIL_PRODUCT"),




		# QUERY
		url(r'^GET_LIST_PRODUCT_BY_COMPANY/$',GET_LIST_PRODUCT_BY_COMPANY,name="GET_LIST_PRODUCT_BY_COMPANY"),
]