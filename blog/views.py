from django.shortcuts import render,get_object_or_404
from.models import Post

def post_list(request):
    posts = Post.objects.filter(status="published")
    return render(request, 'blog/post/list.html',{'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    return render(request, 'blog/post/detail.html',{'posts':posts})



# Create your views here.

