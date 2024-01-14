from django.shortcuts import render
from .models import BlogPost

def blog_index(request):
    # Order the blog posts by publication date in descending order
    posts = BlogPost.objects.all().order_by('-published_date')

    context = {
        'posts': posts
    }

    return render(request, 'blog/blog.html', context)
