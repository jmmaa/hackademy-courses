from django.contrib import admin


# Register your models here.

from .models import Profile


# activity 4
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name", "description"]

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    # this disables the delete option
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Profile, ProfileAdmin)
