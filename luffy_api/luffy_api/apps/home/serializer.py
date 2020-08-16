# Author LZ
# @Time: 2020/8/15 21:12

from rest_framework import serializers
from .models import Banner


class BannerModelSerializer(serializers.ModelSerializer):
	"""轮播广告系列化器"""
	
	# 模型序列化器字段声明
	class Meta:
		model = Banner  # 序列化model名称
		fields = ['image_url', 'link']  # 序列化的字段
