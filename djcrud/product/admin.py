from django.contrib import admin

from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'user', 'created', 'updated')
    list_filter = ('cat_name', 'user', 'created', 'updated')
    search_fields = ('cat_name',)


class PorductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'user', 'created', 'updated')
    list_display_links = ('product_name', 'category', 'user')
    list_filter = ('product_name', 'category', 'user')
    search_fields = ('product_name',)
    # list_editable = ('product_name', 'category', 'user')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, PorductAdmin)
