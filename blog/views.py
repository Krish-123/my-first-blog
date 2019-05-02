from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request,id):
    published_posts = Post.objects.filter(published_date__lte=timezone.now())
    post = get_object_or_404(published_posts,pk=id)

    return render(request,'blog/post_detail.html',{'post':post})