from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.


def error(value):
    if len(value)<10:
        raise ValidationError(
            _("max 10 no is required"),
            params={value:"value"},

        )
    
def mail(value):
    a="@gmail"
    if a not in value:
        raise ValidationError(
            _("invalid email"),
            params={"value":value},
        )
class maclloc(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(validators=[error],max_length=10)
    email=models.CharField(max_length=20,validators=[mail])
    message=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class courses(models.Model):
    image=models.ImageField(upload_to='image/')
    course_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=50)
    banner_image=models.ImageField(upload_to='image/',default='img')
    content_image=models.ImageField(upload_to='image/',default='img')
    content_head=models.CharField(max_length=100,default='heading')
    content=models.CharField(max_length=1000,default='content')
    content_head2=models.CharField(max_length=100,default='none')
    content2=models.CharField(max_length=1000,default='none')
    content_image2=models.ImageField(upload_to='image/',default='none')

    def __str__(self):
        return self.course_name
    

class review(models.Model):
    image=models.ImageField(upload_to='image/')
    name=models.CharField(max_length=50)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name
    


class team(models.Model):
    image=models.ImageField(upload_to='image/')
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    