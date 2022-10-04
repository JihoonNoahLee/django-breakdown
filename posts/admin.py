from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'created_at',
        'updated_at',)
    search_fields = ('title',)
    #list_filter 이런 애도 있음
    # list_display_links
