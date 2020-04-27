from django.contrib import admin

from .models import *

admin.site.register(Department)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'pub_date')
    inlines = [ImageInline]

admin.site.register(Show, ShowAdmin)
