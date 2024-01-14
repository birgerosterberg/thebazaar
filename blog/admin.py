from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

class BlogPostAdmin(SummernoteModelAdmin):  # inherit from SummernoteModelAdmin
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostAdmin)