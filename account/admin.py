from django.contrib import admin
from .models import Profile, UserPersonal_info, UserBio_info

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'code_used', 'active')
    search_fields = ('user__username', 'code')
    list_filter = ('code_used', 'active')

class UserPersonal_infoAdmin(admin.ModelAdmin):
    list_display = ('user', 'iqama_id', 'mobile')
    search_fields = ('user__username', 'iqama_id', 'mobile')

class UserBio_infoAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_position', 'department', 'SCFHS')
    search_fields = ('user__username', 'job_position', 'department', 'SCFHS')
    list_filter = ('job_position', 'department')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserPersonal_info, UserPersonal_infoAdmin)
admin.site.register(UserBio_info, UserBio_infoAdmin)
