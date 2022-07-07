from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import board.views
from . import views

app_name='member'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('board/notice',board.views.notice,name='notice'),
    path('board/news',board.views.news,name='news'),
    path('info', views.info, name='info'),
    path('oauth', views.oauth, name='oauth'),
    path('logout', views.logout, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)