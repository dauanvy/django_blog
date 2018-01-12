from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponseRedirect
from blog.models import Blog
from blog.models import BlogForm

from blog.models import BlogUsers
from blog.models import BlogUsersForm

# Create your views here.
# def index(request):
#     return render(
#         request,
#         'blog/index.html'
#     )

# Form nhap lieu
def index(request):
    data = {}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/success')
    else:
        form = BlogForm()
    list_item = Blog.objects.all()
    data['id'] = None
    data['list_item'] = list_item
    data['form'] = form
    return render(
        request,
        'blog/index.html',
        data
    )

def update_item(request, id):
    data = {}
    try:
        selected_item = Blog.objects.get(pk=id)
        form = BlogForm(instance=selected_item)
    except Blog.DoesNotExist:
        raise Http404("This item not exist.")
    if request.method == 'POST':
        form = BlogForm(request.POST or None, instance=selected_item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/success')
    list_item = Blog.objects.all()
    data['id'] = id
    data['list_item'] = list_item
    data['form'] = form
    return render(
        request,
        'blog/index.html',
        data
    )

def remove_item(request, id):
    data = {}
    try:
        selected_item = Blog.objects.get(pk=id)
        selected_item.delete()
        form = BlogForm()
    except Blog.DoesNotExist:
        raise Http404("This item not exist.")
    list_item = Blog.objects.all()
    data['id'] = None
    data['list_item'] = list_item
    data['form'] = form
    return HttpResponseRedirect('/blog/index', data)

def success(request):
    return render(
        request,
        'blog/success.html'
    )

def users(request):
    data = {}
    if request.method == 'POST':
        form = BlogUsersForm( request.POST )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/success')
    else:
        form = BlogUsersForm()
    list_item = BlogUsers.objects.all()
    data['id'] = None
    data['list_item'] = list_item
    data['form'] = form
    return render(
        request,
        'blog/users.html'
    )