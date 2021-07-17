import datetime

import django.contrib.admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Operation(models.Model):
    name=models.CharField(max_length=50,verbose_name='操作名称',default='')
    description=models.CharField(max_length=50,verbose_name='操作原因',default='')
    operator=models.CharField(max_length=50, blank=True, verbose_name=u"添加者",default='')

    deal_code=models.CharField(max_length=16,default='',verbose_name='业务号')
    from_ips=models.CharField(max_length=100,default='',verbose_name='原始ip')
    to_ips=models.CharField(max_length=100,default='',verbose_name='结果ip')

    operation_time=models.DateTimeField(default=datetime.datetime.now(),verbose_name='操作时间')


    class Meta:
        verbose_name = u'操作日志管理'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

# class Test(models.Model):
#     name = models.CharField(max_length=20)
#
#
# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField(default=0)
#     email = models.EmailField()
#
#     def __unicode__(self):
#         return self.name
#
#
# class Tag(models.Model):
#     contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
#     name = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.name