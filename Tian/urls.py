"""Tian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

import board.views
import member.views

admin.site.site_header = 'AONE HEADER'
admin.site.site_title = 'AONE TITLE'
admin.site.index_title = 'SITE INDEX'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('info.urls')),
    path('board/notice', board.views.notice, name='notice'),
    path('board/news', board.views.news, name='news'),

    path('member/info', member.views.info, name='info'),
    path('member/oauth', member.views.oauth, name='oauth'),
    path('member/logout', member.views.logout, name='logout'),

    path('member/', include('member.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
