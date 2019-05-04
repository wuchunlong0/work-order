# -*- coding: UTF-8 -*-
import os
import sys
import django
import random
import datetime


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission
    from ask.models import Ask
    
    #创建组operatorGroup
    operatorGroup = Group.objects.create(name='Operator')    
    #operatorGroup组添加权限 自定义权限：models.py 
    #operatorGroup.permissions.add(Permission.objects.get(name='查看学员信息表'))
    
    user = User.objects.create_superuser('admin', 'admin@test.com','1234qazx')
    user.save()
    
    user = User.objects.create_user('test1', 'test1@test.com','1234qazx')
    user.is_staff = True
    user.is_superuser = False
    user.save()      
    
    user = User.objects.create_user('test2', 'test2@test.com','1234qazx')
    user.is_staff = True
    user.is_superuser = False
    #user.groups.add(operatorGroup) #用户加入组operatorGroup
    user.save() 
    
    users = User.objects.all()
    OPEERATOR_NUM = 2
    for i in range(OPEERATOR_NUM):
        a = Ask()
        a.name = random.choice(list(users)) #登录用户
        a.title = '%s-%s' %('title',i)
        a.uploadimg = '%s%s' %('/static/upload/upaskimg/', 'imgname.jpg')#数据库保存包含路径的文件名     
        a.edit = '%s-%s' %('wuchunlong',i)      
        a.status = 'noreply' # 没有回答       
        a.save()        

    
   