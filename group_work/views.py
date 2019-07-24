from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, GroupType

def post_list(request):
    posts_all_list = Post.objects.all()
    paginator = Paginator(posts_all_list,10)
    page_num = request.GET.get('page',1)
    page_of_posts = paginator.page(page_num)

    context = {}
    context['page_of_posts'] = page_of_posts
    context['group_types'] = GroupType.objects.all()
    return render_to_response('post_list.html', context)

def post_detail(request, post_pk):
    context = {}
    context['post'] = get_object_or_404(Post, pk=post_pk)
    return render_to_response('post_detail.html', context)

def posts_with_type(request, group_type_pk):
    context = {}
    group_type = get_object_or_404(GroupType, pk=group_type_pk)
    post_of_type = Post.objects.filter(group_type=group_type)
    paginator = Paginator(post_of_type,10)
    page_num = request.GET.get('page',1)
    page_of_posts = paginator.page(page_num)
    
    context['group_type'] = group_type
    context['page_of_posts'] = page_of_posts
    context['group_types'] = GroupType.objects.all()
    return render_to_response('posts_with_type.html', context)