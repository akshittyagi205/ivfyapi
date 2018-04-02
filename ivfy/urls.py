"""ivfy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import androidapi.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^createsession/',androidapi.views.createSession.as_view()),
    url(r'^joinsession/',androidapi.views.joinSession.as_view()),
    url(r'^businesssignup/',androidapi.views.businessRegister.as_view()),
    url(r'^businesslogin/',androidapi.views.businessLogin.as_view()),
    url(r'^getbusinessnames/',androidapi.views.getBusinessNames.as_view()),
    url(r'^fillekyc/',androidapi.views.fillEKYC.as_view()),
    url(r'^viewekyc/',androidapi.views.seeEKYC.as_view()),    
]
