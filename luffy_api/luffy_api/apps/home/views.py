from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializer import BannerModelSerializer
from luffy_api.settings import constants


class BannerListAPIView(ListAPIView):  # 自动导包
	queryset = Banner.objects.filter(is_deleted=False, is_show=True).order_by('-orders',
																			  '-id')[:constants.BANNER_LENGTH]
	serializer_class = BannerModelSerializer
