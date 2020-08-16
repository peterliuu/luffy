# Author LZ
# @Time: 2020/8/15 21:17
from django.urls import path
from . import views

urlpatterns = [
	path(r'banner/', views.BannerListAPIView.as_view())
]