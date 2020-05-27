#LIAM CORLEY 2020
#Admin registration and form modifications

from django.contrib import admin

from .models import *

#Register department to django admin
admin.site.register(Department)

#Create inline image create admin
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

#Define attributes of ShowAdmin
class ShowAdmin(admin.ModelAdmin):
    #Set fields to display in Show list
    list_display = ('title', 'department', 'created_at')
    #Add ImageInLine to Show create
    inlines = [ImageInline]

#Resiter Show to django admin
admin.site.register(Show, ShowAdmin)
