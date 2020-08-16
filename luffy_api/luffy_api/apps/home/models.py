from django.db import models


# Create your models here.
class Banner(models.Model):
	"""轮播图"""
	# 模型字段
	title = models.CharField(max_length=500, verbose_name='广告标题')
	link = models.CharField(max_length=500, verbose_name='广告链接')
	# 保存图像文件的字段,数据库中是以某个路径下的文件名保存 upload_to设置文件上传的子目录,设置可不为空，防止修改数据bug
	image_url = models.ImageField(upload_to='banner', null=True, blank=True, max_length=255, verbose_name="广告图片")
	remark = models.TextField(verbose_name="备注信息")
	is_show = models.BooleanField(default=False, verbose_name='是否显示')
	orders = models.IntegerField(default=1, verbose_name='排序')
	is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
	
	# 表信息声明
	class Meta:
		db_table = 'ly_banner'
		verbose_name = '轮播广告'
		verbose_name_plural = verbose_name
	
	# 自定义方法[自定义字段或者工具方法]
	def __str__(self):
		return self.title
