from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def post_list(request):

    index = request.GET.get('index')
    search = request.GET.get('search')

    if search:
        post = Post.objects.filter(
            Q(title__contains=search) | 
            Q(text__contains=search)
        ).order_by('create_date')

    elif index:   
        post = Post.objects.filter(index=index)

    else:
        post = Post.objects.filter(index='1')
    
    context = {'post': post}
    return render(request, 'blog/post_list.html', context)

def sobre(request):
    return render(request, 'blog/sobre.html', {})

def disp_moveis(request):
    return render(request, 'blog/disp_moveis.html', {})