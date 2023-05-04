"""mediproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from mediapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('userindex', index), 
    path('register',reg),
    path('login',log), 
    path('logout',logout),
    path('adminindex',adminindex),
    path('userindex',userindex),
    path('doctorindex',doctorindex),
    path('viewdoctors',viewdoctor),
    path('viewtrainees',viewtrainee),
    path('approve/<int:id>', approve),
    path('addquestion',addquestion),
    path('viewquestionadmin',viewquesadmin),
    path('approveadmin/<int:id>',approveadmin),
    path('viewapproveqstn',viewapproveqstn),
    # path('addreplay/<int:id>',addreplay),
    path('addnutrition',addnutrition),
    path('viewnutrition',viewnutrition),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)