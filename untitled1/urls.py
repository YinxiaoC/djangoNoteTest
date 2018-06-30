"""untitled1 URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from note import views
from note import urls
urlpatterns = [
    #path('admin/', admin.site.urls),

    #管理员
    url(r'^admin/', admin.site.urls),

    # #主页
    # url(r'^$', views.index, name='index'),
    #
    # #显示所有主题
    # url(r'^topics/$', views.topics, name='topics'),
    # # 特定主题的详细页面
    # url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'', include(urls, namespace='note'))

]
