from typing import Any
from django.shortcuts import render
from .models import maclloc
from . import models
from django.http import HttpResponse
from .forms import MacllocForm
from django import template
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# def index(request):
#     return HttpResponse("Hello , world. you're at polls's index")


# def mac(request):
#     form=models.courses.objects.all()[0:4]
#     context={'courses':form}
#     return render(request, 'maclloc.html',context)


# def courses(request):
#     form=models.courses.objects.all()
#     context={'courses':form}
#     return render(request, 'courses.html',context)


# def coursesDetail(request, id):
#     data=models.courses.objects.get(id=id)
#     list=data.content.split('&')
#     context={'courses':data,
#              'list':list}
#     return render(request, 'coursesDetail.html',context)


# def contact(request):
#     if request.method=="POST":
#         form=MacllocForm(request.POST)
#         if form.is_valid():
#             form.save
#     else:
#         form=MacllocForm()
#     context={'form':form}
#     return render(request, 'contact.html',context)


class index(View):
    def get(self, request, *args, **kwargs):
        id=kwargs['id']
        print(kwargs)
        return HttpResponse("Hello , world. you're at polls's index ")
    

class mac(View):
    def get(self,request,*args,**kwargs):
        form=models.courses.objects.all()[0:4]
        form1=models.review.objects.all()
        context={'courses':form,'review':form1}
        return render(request,'maclloc.html',context)

# class mac(request):
#     form=models.review.objects.all()
#     context={'form':form}

    # def get(self,request,*args,**kwargs):
    #     student=models.review.objects.all()
    #     context={'review':student}
    #     return render(request,'maclloc.html',context)
    

# class courses(View):
#     def get(self,request,*args,**kwargs):
#         form=models.courses.objects.all()
#         context={'courses':form}
#         return render(request, 'courses.html',context)

class coursesListView(ListView):
    model=models.courses
    template_name='courses.html' # default : courses_list.html
    context_object_name='courses' # default : object_list

# class coursesDetail(View):
#     def get(self,request,*args,**kwargs):
#         data=models.courses.objects.get(id=kwargs['id'])
#         # id=kwargs['id']
#         context={'courses':data}
#         return render(request, 'coursesDetail.html',context)
    
class coursesDetail(DetailView):
    model=models.courses
    template_name='coursesDetail.html' #default : courses_detail.html
    context_object_name='courses'  #default : object

    def get_context_data(self, **kwargs):
        context=super(coursesDetail,self).get_context_data(**kwargs)
        context['list']=self.get_object().content.split('&')
        return context
        

class contact(View):
    def post(self,request,*args,**kwargs):
        form=MacllocForm(request.POST)
        if form.is_valid():
            form.save()
        context={'form':form}
        return render(request,'contact.html',context)
    
    def get(self,request,*args,**kwargs):
        form=MacllocForm()
        context={'form':form}
        return render(request,'contact.html',context)
    
class about(ListView):
    model=models.team
    template_name='about.html' # default : courses_list.html
    context_object_name='team' # default : object_list
