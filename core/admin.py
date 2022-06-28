from django.contrib import admin

from core.models import CustomChampion, CustomItem

# Register your models here.


# REGISTER MODEL FOR ADMIN PANEL
admin.site.register(CustomChampion)
admin.site.register(CustomItem)