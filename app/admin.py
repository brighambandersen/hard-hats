from django.contrib import admin
from app.models import Profile, Employee


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Employee)
