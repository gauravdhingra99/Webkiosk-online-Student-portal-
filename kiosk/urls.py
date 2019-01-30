from django.urls import path,include
from kiosk import views

urlpatterns = [
    path('',views.user,name='user'),
    path('',views.index,name="wrong"),
    #path('',views.personal_info,name='personal_info'),
]
