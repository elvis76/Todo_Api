from django.contrib import admin
from .models import Todo

# Register your models here.

admin.site.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["task", "status", 'user',"date","date_created"]
    list_editable= ['status']