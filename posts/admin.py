from django.contrib import admin

from .models import BlogPost, CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "email", "username", "role"]


class BlogPostAdmin(admin.ModelAdmin):
    fields = ["title", "content", "author"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
