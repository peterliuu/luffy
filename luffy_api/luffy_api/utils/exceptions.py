# Author LZ
# @Time: 2020/8/13 23:28

from rest_framework.views import exception_handler
from django.db import DatabaseError
import logging
from rest_framework.response import Response
from rest_framework import status
from redis import RedisError
# 获取django日志对象
logger = logging.getLogger("django")


def custom_exception_handler(exc, content):
	"""
	自定义异常处理
	:param exc: 本次请求发生时的异常信息对象
	:param content: 本次请求发送异常的执行上下文[本次请求的request对象，异常发送的时间，行号等]
	:return:
	"""
	response = exception_handler(exc, content)
	if response is None:
		"""来到这里只有2中情况：要么程序没出错，要么就是出错了django或者restframework不识别"""
		view = content["view"]  # 从上下文获取view视图
		if isinstance(exc, DatabaseError):
			# 数据库异常
			logger.error("[%s] %s" % (view, exc))
			response = Response({"message": "服务器内存错误，请联系客服工作人员！"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
	return response















