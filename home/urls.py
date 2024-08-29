"""
URL configuration for unknow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_user/',register_user.as_view()),
    path('login_user/',login_user.as_view()),
    path('login/',verify_user),
    path('forgot-password/',forgotpassword.as_view()),
    path("reset-password/",reset_password),
    path('profile/',profiledata.as_view()),
    path('update_peronalprofile/',update_peronalprofile.as_view()),
    path('brancheslist/',get_branches.as_view()),
    path("getstudentsformarks/",studentListformarks),
    path("Enterstudentmarks/",enterstudetnmarks.as_view()),
    path('viewmarks/',Dispalymarks.as_view()),
    path('viewattendance/',get_attendance.as_view()),
    path('sendmessage/',send_message.as_view()),
    path('receivemessage/',receiver_message.as_view()),
    path('sendpdf/',send_pdf.as_view()),
    path('receivepdf/',receiver_message_pdf.as_view()),
    path('getavailablebooks/',displayavailablebooks.as_view()),
    
    
]
