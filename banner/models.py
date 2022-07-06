
# Create your models here.
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

class Mainbanner(models.Model):
    image_1 = models.ImageField(upload_to='main_banner/%Y%M%d', verbose_name="#1이미지")
    first_copy = models.CharField(blank=True, null=True, max_length=50, verbose_name="#1카피")
    first_label=models.CharField(blank=True, null=True, max_length=50,verbose_name="#1레이블")

    image_thumbnail_1=ImageSpecField(source='image_1', processors=[ResizeToFill(1903, 400)],format='JPEG')

    image_2 = models.ImageField(upload_to='main_banner/%Y%M%d', verbose_name="#2이미지")
    second_copy = models.CharField(blank=True, null=True, max_length=50, verbose_name="#2카피")
    second_label=models.CharField(blank=True, null=True, max_length=50,verbose_name="#2레이블")

    image_thumbnail_2 = ImageSpecField(source='image_2', processors=[ResizeToFill(1903, 400)], format='JPEG')

    image_3 = models.ImageField(upload_to='main_banner/%Y%M%d', verbose_name="#3이미지")
    third_copy = models.CharField(blank=True, null=True, max_length=50, verbose_name="#3카피")
    Third_label=models.CharField(blank=True, null=True, max_length=50,verbose_name="#3레이블")

    image_thumbnail_3 = ImageSpecField(source='image_3', processors=[ResizeToFill(1903, 400)], format='JPEG')

    created_date = models.DateTimeField(default=timezone.now,verbose_name="작성일")
    published_date = models.DateTimeField(blank=True, null=True,verbose_name="수정일")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class subbanner(models.Model):
    subbanner_select = {('info', 'info')}
    subbanner_part = models.CharField(max_length=30, choices=subbanner_select,verbose_name="노출영역")
    image = models.ImageField(upload_to='sub_banner/%Y%M%d', verbose_name="이미지")
    copy=models.CharField(blank=True, null=True, max_length=50,verbose_name="카피")
    label = models.CharField(blank=True, null=True, max_length=50, verbose_name="레이블")
    image_thumbnail=ImageSpecField(source='image', processors=[ResizeToFill(1294, 289)],format='JPEG')
    created_date = models.DateTimeField(default=timezone.now,verbose_name="작성일")
    published_date = models.DateTimeField(blank=True, null=True,verbose_name="수정일")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class topbanner(models.Model):
    subbanner_select = {('info', 'info')}
    subbanner_part = models.CharField(max_length=30, choices=subbanner_select,verbose_name="노출영역")
    image = models.ImageField(upload_to='sub_banner/%Y%M%d', verbose_name="이미지")
    image_thumbnail=ImageSpecField(source='image', processors=[ResizeToFill(1294, 100)],format='JPEG')
    created_date = models.DateTimeField(default=timezone.now,verbose_name="작성일")
    published_date = models.DateTimeField(blank=True, null=True,verbose_name="수정일")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# Create your models here.
