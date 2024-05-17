from django.contrib import admin
from django.conf import settings 
from django.urls import path
from .import views
from django.conf.urls.static import static
 

urlpatterns =[
    path("poll/<id>",views.index.as_view(),name='index'),
    path("", views.mac.as_view(), name='maclloc'),
    path("courses/", views.coursesListView.as_view(), name='courses'),
    path("courses/<pk>", views.coursesDetail.as_view(), name='coursesDetail'),
    path("contact/", views.contact.as_view(), name='contact'),
    path("about/",views.about.as_view(),name='about')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


