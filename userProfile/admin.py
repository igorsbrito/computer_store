from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')

    fieldsets = (('User Data', {'fields': ('full_name', 'email')}),)

    def has_add_permission(self, request):
        return False


admin.site.register(User, UserAdmin)