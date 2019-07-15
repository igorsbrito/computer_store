from django.contrib import admin
from .models import Computer


# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['mother_board', 'cpu', 'ram_memory', 'video_card', 'belong']

    fieldsets = [('Computer Data',
                  {'fields': [
                      'mother_board', 'cpu', 'ram_memory', 'belong', 'video_card', 'created_date']}
                  )]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Computer, ComputerAdmin)
