from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Comment

# Create your views here.
def add_blogs(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('images')

        if title:
            save_blog = Blog(title=title, content=content, images=image)
            save_blog.save()
            return redirect("showblog")

    return render(request,"add_blogs.html")


def showblog(request):
    all_blogs = Blog.objects.all()

    context = {
        "allblog" : all_blogs
    }
    return render(request,"showblog.html",context)


def add_comment(request,id):
    single_blog = get_object_or_404(Blog,id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")

        save_comment = Comment.objects.create(blog=single_blog,name=name,email=email,comm=comment)
        save_comment.save()
        return redirect("showblog")
    
    all_comments = Comment.objects.filter(blog=single_blog)
    
    context = {
        "single_blog" : single_blog,
        "all_comments" : all_comments,
    }

    return render(request,"add_comment.html",context)