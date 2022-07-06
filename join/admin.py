from django.contrib import admin
from .models import member_info

# Register your models here.
class class_member_info(admin.ModelAdmin):
    list_display = ['u_id','u_properties','u_nickname','u_email','u_phone_number','u_age_range','u_gender','u_profile_image','u_thumbnail_image','u_profile_image_url','u_thumbnail_image_url','u_use','note','u_connected_at','published_date']
    list_display_links =['u_id','u_properties','u_nickname','u_email','u_phone_number','u_age_range','u_gender','u_profile_image','u_thumbnail_image','u_profile_image_url','u_thumbnail_image_url','u_use','note','u_connected_at','published_date']
    ordering = ['u_id','u_properties','u_nickname','u_email','u_phone_number','u_age_range','u_gender','u_profile_image','u_thumbnail_image','u_profile_image_url','u_thumbnail_image_url','u_use','note','u_connected_at','published_date']
    list_filter = ['u_id','u_properties','u_nickname','u_email','u_phone_number','u_age_range','u_gender','u_profile_image','u_thumbnail_image','u_profile_image_url','u_thumbnail_image_url','u_use','note','u_connected_at','published_date']
    search_fields = ['u_id','u_properties','u_nickname','u_email','u_phone_number','u_age_range','u_gender','u_profile_image','u_thumbnail_image','u_profile_image_url','u_thumbnail_image_url','u_use','note','u_connected_at','published_date']

admin.site.register(member_info,class_member_info)
# Register your models here.


