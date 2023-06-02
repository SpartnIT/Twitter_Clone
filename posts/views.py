from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm



# Create your views here.
def index(request):
    # If the method is POST 
    if request.method == 'POST':
       form = PostForm(request.POST, request.FILES)
       # If the method is valid
       if form.is_valid():
           # Yes, save
           form.save()

           # Redirect to homepage
           return HttpResponseRedirect('/')
       
       else:   
           #No, Show error
           return HttpResponseRedirect({form.errors.as_json})




    #get all posts, limit 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    #show
    return render(request, 'posts.html',{'posts':posts})

def delete(request, post_id):
    # Find post
    posts = Post.objects.get(id = post_id)
    posts.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    if request.method == "GET":
        posts = Post.objects.get(id = post_id)
        return render(request,"edit.html", {"posts":posts})
    if request.method == "POST":
        edit_post = Post.objects.get(id = post_id)
        form = PostForm(request.Post, request.FILES,instance = edit_post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Not Valid')
        
x = 0  
def likes(request,post_id):
    like_tweet = Post.objects.get(id = post_id)
    # Fetches all objects(posts made) in the Post class
    #x = 0
    #species variable scope
    global x
    if x == 0:
        like_tweet.like = 1
        x = 1
    elif x == 1:
        like_tweet.like = 0
        x = 0
    # like_tweet.likes = like_tweet.likes + 1
    like_tweet.save()
    return HttpResponseRedirect('/')

#model for image and like button in models.py
#add two function for edit and like button in views.py
#add cloudinary configration in settings.py
#add the urls for edit and like button in urls.py in app
#in template you need to add edit.html
#download images for the application
#style.css

