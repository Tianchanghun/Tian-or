from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import board.views
from . import views

admin.site.site_header = 'AONE HEADER'
admin.site.site_title = 'AONE TITLE'
admin.site.index_title = 'SITE INDEX'

app_name = 'board'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('board/notice', board.views.notice, name='notice'),
    path('board/news', board.views.news, name='news'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
