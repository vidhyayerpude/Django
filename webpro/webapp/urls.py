from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('accountsetting/', views.accountsetting, name='accountsetting'),
    path('training/', views.training, name='training`   '),
    path('userform/', views.userForm, name='userform`   '),

]

admin.site.site_header = "vidhya Admin"
admin.site.site_title = "vidhya Admin Portal"
admin.site.index_title = "Welcome to vidhya Researcher Portal"
