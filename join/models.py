import json
import time
import datetime
import uuid
import hmac
import hashlib
import requests

from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

class member_info(models.Model):
    u_id=models.CharField(max_length=30,unique=True,verbose_name="아이디") #아이디
    u_properties=models.CharField(max_length=30,blank=True, null=True,verbose_name="닉네임") #닉네임
    u_nickname=models.CharField(max_length=30,blank=True, null=True,verbose_name="닉네임") #닉네임
    u_email=models.CharField(max_length=100,blank=True, null=True,verbose_name="이메일")#이메일
    u_phone_number=models.CharField(max_length=100,blank=True, null=True,verbose_name="핸드폰")#핸드폰
    u_age_range=models.CharField(max_length=100,blank=True, null=True,verbose_name="연령대")#연령대
    u_gender=models.CharField(max_length=100,blank=True, null=True,verbose_name="성별")#성별
    u_profile_image=models.CharField(max_length=100,blank=True, null=True,verbose_name="이미지 주소") #이미지 주소
    u_thumbnail_image=models.CharField(max_length=100,blank=True, null=True,verbose_name="작은 이미지 주소") #작은 이미지 주소
    u_profile_image_url=models.CharField(max_length=100,blank=True, null=True,verbose_name="작은 이미지 주소") # 이미지 주소
    u_thumbnail_image_url=models.CharField(max_length=100,blank=True, null=True,verbose_name="이미지 주소") #작은 이미지 주소
    u_use = models.BooleanField(default=True, verbose_name="사용여부")  # 사용여부
    note=RichTextUploadingField(blank=True, null=True,verbose_name="비고") #비고
    u_connected_at=models.DateTimeField(default=timezone.now,verbose_name="등록일")
    published_date = models.DateTimeField(blank=True, null=True,verbose_name="수정일")
    def publish(self):
        self.published_date = timezone.now()
        self.save()



