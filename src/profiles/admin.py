from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from .models import Profile, Relationship
# Register your models here.


class ProfileAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Relationship)
