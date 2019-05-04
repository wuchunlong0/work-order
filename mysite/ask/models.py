# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#本框架 数据库名称不能用User，否则出错！
from django.contrib.auth.models import User
from django.db import models
import datetime
#提问
class Ask(models.Model):
    name = models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True)    
    title = models.CharField(max_length = 60, blank=True, null=True)
    uploadimg = models.FileField(upload_to =  './static/upload/upaskimg/',blank=True, null=True)
    edit = models.CharField(max_length = 600, blank=True, null=True)
    status = models.CharField(max_length = 2, blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)  
    def __str__(self):
        return self.name
#答复
class Answer(models.Model):
    name = models.ForeignKey(User, on_delete=models.PROTECT,blank=True, null=True)
    title = models.CharField(max_length = 60,blank=True, null=True)
    uploadimg = models.FileField(upload_to =  './static/upload/upanswerimg/',blank=True, null=True)#创建该目录,存放上传的文件    
    edit = models.CharField(max_length = 600,blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True) #日期含时间    
    def __str__(self):
        return self.name

    