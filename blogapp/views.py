from django.shortcuts import render
from .models import Blog

# Create your views here.
def add_blogs(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('images')

        if title:
            save_blog = Blog(title=title, content=content, images=image)
            save_blog.save()

    return render(request,"add_blogs.html")