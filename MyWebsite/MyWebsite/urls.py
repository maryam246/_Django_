"""
URL configuration for MyWebsite project.

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
from django.urls import path
from MyWebsite import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name='home'),
    path('features/',views.features, name='features'),
    path('services/',views.services, name='services'),
    path('submitform/',views.submitform, name='submitform'),
    path('evenodd/',views.evenodd),
    path('markssheet/',views.markssheet),
    path('contact/',views.contact, name='contact'),
    path('userform/',views.userform, name='userform'),
    path('newsDetails/<slug>',views.newsDetails),
    path('saveEnquiry/',views.saveEnquiry, name='saveEnquiry')

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)