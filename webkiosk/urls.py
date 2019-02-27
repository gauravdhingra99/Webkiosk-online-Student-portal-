"""webkiosk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from kiosk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name="login"),
    path('user/',views.user,name='user'),
    path('personal_info/',views.personal_info,name="personal_info"),
    path('regsinfo/',views.regsinfo,name="regsinfo"),
    path('feereciept/',views.feereciept,name="feereciept"),
    path('feepayrec/',views.feepayrec,name="feepayrec"),
    path('Attendance/',views.Attendance,name="Attendance"),
    path('CGPA/',views.CGPA,name="CGPA"),
    path('wrong/',include('kiosk.urls')),
    path('subjregister/',views.subjregister,name='subjregister'),
    path('subjfaculty/',views.subjfaculty,name='subjfaculty'),
    path('displinary/',views.displinary,name='displinary'),
    path('exammarks/',views.exammarks,name='exammarks'),
    path('showattendance/w+/',views.Attendance,name='attendenceshowall'),
    ]
