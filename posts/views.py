from django.shortcuts import render,redirect
from . models import Post
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts=Post.objects.all().order_by("-date")
    return render(request,"posts/posts_list.html",{'posts':posts} )  #this posts will used for loop in views allobjects

def post_page(request,slug):
    post=Post.objects.get(slug=slug)   #this will give matching slug 
    return render(request,"posts/post_page.html",{'post':post} )  #this posts will used for loop in views allobjects

@login_required(login_url="/users/login/")
def new_post(request):
    if request.method=='POST': 
        form=forms.CreatePost(request.POST, request.FILES)  
        if form.is_valid(): 
            newpost=form.save(commit=False)
            newpost.auther=request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form=forms.CreatePost()
    return render(request,"posts/new_post.html", {"form":form})
