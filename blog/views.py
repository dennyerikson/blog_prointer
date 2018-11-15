from django.shortcuts import render
from .models import *

# Create your views here.
def post_list(request):
    post = Post.objects.all()
    
    context = {'post': post}
    return render(request, 'blog/post_list.html', context)
