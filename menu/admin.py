from django.contrib import admin
from menu.models import Menu, Item


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title', 'slug')
        }),
    )
