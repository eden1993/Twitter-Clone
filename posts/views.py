from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # If the method is valid
        if form.is_valid():
            # Yes, save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    # Get all posts. limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20] 

    #Show
    return render(request, 'posts.html', {'posts': posts})
      

def delete(request, post_id):
    #output = 'POST ID is ' + str(post_id)
    #return HttpResponse(output)
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
