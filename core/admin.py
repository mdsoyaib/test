

from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from core.models import Product

admin.site.unregister(Group)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity")
