from django.contrib import admin
from .models import Post, Jobs

# Post admin settings
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}

# Jobs Admin Settings
class JobsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title', )}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Jobs)