from django.urls import path
from . import views	
  

urlpatterns=[
        path('',views.blog_list,name='blog_list'),
        path('create/',views.blog_create,name='blog_create'),
        path('<int:blog_id>/edit/',views.blog_edit,name='blog_edit'),
        path('<int:blog_id>/delete/',views.blog_dlt,name='blog_dlt'),
        path('register/',views.register,name='register'),
]

