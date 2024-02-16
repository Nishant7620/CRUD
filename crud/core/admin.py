from django.contrib import admin
from .models import Model
# Register your models here.

@admin.register(Model)
class HomeAdmin(admin.ModelAdmin):
    list_display = ["id","name","heroic_name"]