from django.contrib import admin
from .models import Post

#postadmin을 등록한 거
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']