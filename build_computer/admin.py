from django.contrib import admin
from .models import Computer


# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ['mother_board', 'cpu', 'ram_memory', 'video_card', 'belong']

    fieldsets = [('Computer Data',
                  {'fields': [
                      'mother_board', 'cpu', 'ram_memory', 'belong', 'video_card', 'created_date']}
                  )]


admin.site.register(Computer, ComputerAdmin)
