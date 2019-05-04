# -*- coding: utf-8 -*-
# 1、新建目录下一定要有__init__.py文件，否则不能被其它文件引用、不能沿路径读写文件。from ... 。
# 2、urls.py中,设置第一级路由名ask。 在.../mysite/mysite/urls.py中  url(r'^ask/', include('account.ask.urls')),
# 3、admin.py中,设置数据库显示。在.../mysite/account/admin.py中 @admin.register(Technologyask) ...
# 4、templates中,增加模板文件目录/ask
from __future__ import unicode_literals
import datetime
import os
import json
from django.shortcuts import render
from django.http.response import HttpResponseRedirect,HttpResponse,StreamingHttpResponse
from .models import Ask,Answer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from myAPI.pageAPI import djangoPage,PAGE_NUM,toInt #,django_Page
#from blog.myAPI.sortedAPI import sorted_listdict
# from blog.myAPI.searchAPI import SearchTitle,SearchTagTitle
from django.contrib.auth.models import User


 
class  issue:             #类    
    def speak(self):   #方法                
        print ("hello!") 
#获得让每一个问题都被解决参数函数 round( x [, n]  )方法返回浮点数x的四舍五入值   2016.11.09
def askProportions(request):
    askProportion =  issue() #使用类
    recordcount = Ask.objects.all().count()#问总数
    if recordcount == 0:
        askProportion.recordcount = 0
        askProportion.percentage = 0
        askProportion.nopercentage = 0 
        return askProportion
    reply = Ask.objects.filter(status = 'reply').count()#已经回答数
    askProportion.reply = str(reply)
    percentage = round(reply*100.0/float(recordcount),2)# 保留2位小数 已经回答数 %
    askProportion.recordcount = str(recordcount)
    askProportion.percentage = str(percentage)
    askProportion.noreply = str(recordcount - reply)  #未回答
    askProportion.nopercentage = round((100.0 - percentage),2) #未回答 %
    return askProportion

#提问 写入数据库 http://localhost:8000/ask/ask/
#@login_required
def ask(request):
    os_dir = os.getcwd()   
    imgpath =  '%s/static/upload/upaskimg/' %(os_dir)        
    if request.method == 'POST':
        title = request.POST['title']
        istitle = Ask.objects.filter(title = title)        
        if istitle: #提问标题唯一，不重名
            messages.info(request, 'Title is already in use.')
            return HttpResponseRedirect('/ask/ask/')        

        MyImg = request.FILES.get("upImg", None)     
        if not MyImg:
            messages.info(request, '警告：没有获得上传图像!')
            return HttpResponseRedirect('/ask/ask/')
          
        title_imgname = '%s.jpg' %(title)
        # 保存上传文件
        save_upimg(imgpath,MyImg,title_imgname) 
        shutil.copy('%s%s' %(imgpath,title_imgname),'%s/static_common/upload/upaskimg/' %(os_dir) ) 
        # 写入数据库        
        a = Ask()
        a.name = request.user, #登录用户
        a.title = title,
        a.uploadimg = '%s%s' %('/static/upload/upaskimg/', title_imgname),#数据库保存包含路径的文件名     
        a.edit = request.POST['edit'],       
        a.status = 'noreply',# 没有回答       
        a.save()        
        return HttpResponseRedirect('/ask/list/')   
    askProportion = askProportions(request)
    return  render(request, 'ask/ask.html', context=locals()) 

def Ask_tag_titleask(cleanData):
    tag = cleanData.get('tag','')
    titleask = cleanData.get('titleask','')
    return SearchTagTitle(Ask,tag,titleask).values()

#显示 全部提问 http://localhost:8000/ask/list/
def list(request,page):
    ask_list = Ask.objects.all()
    #askProportion = askProportions(request)    
    return  render(request, 'ask/list.html', context=locals()) 

#@login_required
# def list(request,page):
#     placeholder = u"社区留言板 标题"    
#     page = toInt(page) 
#     if request.method != 'POST':
#         cleanData = request.GET.dict()
#         q = cleanData.get('q','')
#         ask_list = SearchTitle(Ask,q) if q else  sorted_listdict(Ask_tag_titleask(cleanData))                 
#     else:
#         cleanData = request.POST.dict()   
#         ask_list = Ask_tag_titleask(cleanData)
#     ask_list,pageList, num_pages, page,offset,queryString = django_Page(request,ask_list ,page,PAGE_NUM)  #调用分页函数                
#     askProportion = askProportions(request)    
#     return  render(request, 'ask/list.html', context=locals()) 
    

#待回复（还没有回答的问题）http://localhost:9000/ask/noanswer/
def noanswer(request,page):
    page = toInt(page)
    ask_list = Ask.objects.filter(askstatus='noreply')      
    ask_list,pageList, num_pages, page,offset,queryString = django_Page(request,ask_list ,page,PAGE_NUM)  #调用分页函数                    
    askProportion = askProportions(request) 
    return  render(request, 'blog/ask/list.html', context=locals()) 


#回答  写入数据库 http://localhost:8000/ask/answer/?titleask=%E5%A6%82%E4%BD%95%E6%8F%90%E9%97%AE%EF%BC%9F
#@login_required
def answer(request,page):
    page = toInt(page)
    titleask = request.GET.get('titleask','')
    if  titleask == '':
        messages.info(request, u'Answer GET titleask is a NULL.' )
        return  render(request, 'blog/ask/ask.html', context=locals()) 
    if request.method == 'POST':
        editor = request.POST['editor']
        titleask = request.POST['titleask']
        askrname = request.user #登录用户
        if titleask=='':
            messages.info(request, u'Answer POST titleask is a NULL. ')
            return  render(request, 'blog/ask/answer.html', context=locals()) 
        else:
            answernumber = str(int(Ask.objects.get(titleask = titleask).answernumber)+1)
            browsernumber = str(int(Ask.objects.get(titleask = titleask).browsernumber)+1)       
        askstatus = 'noreply' if answernumber == '0' else 'reply'
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        answers = Answer(titleask=titleask, askrname=askrname, \
            editor=editor, answernumber = answernumber,browsernumber = browsernumber, date=date)
        Ask.objects.filter(titleask = titleask).update(askstatus = askstatus,answernumber = answernumber)       
        answers.save()    
    browsernumber = str(int(Ask.objects.get(titleask = titleask).browsernumber)+1)
    Ask.objects.filter(titleask = titleask).update(browsernumber = browsernumber)       
    ask_list = Ask.objects.filter(titleask = titleask)    
    answer_list = Answer.objects.filter(titleask = titleask)
    answer_list, pageList, num_pages, page,offset,queryString = django_Page(request,answer_list,page,PAGE_NUM)  #调用分页函数                  
    return  render(request, 'blog/ask/answer.html', context=locals()) 
