from django.contrib import admin

from .models import *

class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published')
    list_display_links = ('id','title')
    search_fields = ('title', 'content')
    list_filter = ('id', 'title')

admin.site.register(Faq,FaqAdmin)