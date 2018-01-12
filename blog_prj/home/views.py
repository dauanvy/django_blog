# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.messages import constants as messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.db.models import Q

from home.models import Category
from home.models import CategoryForm
from home.models import Tags
from home.models import TagsForm
from home.models import Users
from home.models import UsersForm

#Form nhap lieu
def index(request):
    data = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = CategoryForm()
    list_item = Category.objects.all()
    data['id'] = None
    data['list_item'] = list_item
    data['form'] = form
    paginator = Paginator(list_item, 6)
    try:
    	page = int(request.GET.get('page', '1'))
    except:
    	page = 1
    try:
    	list_item = paginator.page(page)
    except(EmptyPage, InvalidPage):
        list_item = paginator.page(paginator.num_pages)
    return render_to_response('home/index.html', {'list_item': list_item, 'form': form}, context_instance=RequestContext(request))

def category_cat(request):
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = CategoryForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Category()
			newdoc.title = request.POST['title']
			newdoc.content = request.POST['content']
			newdoc = form.save(commit=False)
			newdoc.save()
			return HttpResponseRedirect('category_cat')
	else:
		form = CategoryForm()
	list_item = Category.objects.all()
	return render_to_response(
		'home/category.html',
		{'list_item': list_item, 'form': form},
		context_instance=RequestContext(request)
	)

def update_cat(request, id):
	data = {}
	try:
		selected_item = Category.objects.get(pk=id)
		form = CategoryForm(instance=selected_item)
	except Category.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = CategoryForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/category_cat')
	list_item = Category.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(
		request,
		'home/category_form.html',
		data
	)

def remove_cat(request, id):
	data = {}
	try:
		selected_item = Category.objects.get(pk=id)
		selected_item.delete()
		form = CategoryForm()
	except Category.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Category.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/category_cat', data)

def success(request):
	return render(
		request,
		'home/success.html'
	)

def category_input(request):
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = CategoryForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Category()
			newdoc.title = request.POST['title']
			newdoc.content = request.POST['content']
			newdoc = form.save(commit=False)
			newdoc.save()
			return HttpResponseRedirect('/category_cat')
	else:
		form = CategoryForm()
	list_item = Category.objects.all()
	return render_to_response(
		'home/category_form.html',
		{'list_item': list_item, 'form': form},
		context_instance=RequestContext(request)
	)

def tags(request):
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	if request.method == 'POST':
		form = TagsForm(request.POST)
		if form.is_valid():
			newdoc = Tags()
			newdoc.name = request.POST['name']
			newdoc.save()
			return HttpResponseRedirect('/tags')
	else:
		form = TagsForm()
	tags = Tags.objects.all()
	return render_to_response(
		'home/tags.html',
		{'tags': tags, 'form': form},
		context_instance=RequestContext(request)
		)
def update_tags(request, id):
	data = {}
	try:
		selected_item = Tags.objects.get(pk=id)
		form = TagsForm(instance=selected_item)
	except Tags.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = TagsForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/tags')
	tags = Tags.objects.all()
	data['id'] = id
	data['tags'] = tags
	data['form'] = form
	return render(
		request,
		'home/tags.html',
		data
		)

def remove_tags(request, id):
	try:
		selected_item = Tags.objects.get(pk=id)
		selected_item.delete()
# 		form = TagsForm()
	except Tags.DoesNotExist:
		raise Http404("This item not exist.")
# 	tags = Tags.objects.all()
	return HttpResponseRedirect('/tags')

#Form nhap lieu
def login(request):
	form = UsersForm(request.POST)
	s = request.session.get('users_id', None)
	if not s:
		return HttpResponseRedirect('/auth')
	data = {}
	data['error_massage']=""
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		password_password =  make_password(password)
		try:
			users = Users.objects.get(email=email)
			if users.email == email and check_password("password", password_password):
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/login')
			else:
				return HttpResponseRedirect('/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/auth')
	else :
		form = UsersForm()
	list_item = Users.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(
		request,
		'home/login.html',
		data
	)

def update_item(request, id):
	data = {}
	try:
		selected_item = Users.objects.get(pk=id)
		form = UsersForm(instance=selected_item)
	except Users.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = UsersForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login')
	list_item = Users.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(
		request,
		'home/login.html',
		data
	)

def remove_item(request, id):
	data = {}
	try:
		selected_item = Users.objects.get(pk=id)
		selected_item.delete()
		form = UsersForm()
	except Users.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Users.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/login', data)

#Ham lay du lieu tu database
def auth(request):
	s = request.session.get('users_id',None)
	if s:
		return HttpResponseRedirect('/category_cat')
	if request.method == 'POST':
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		try:
			users = Users.objects.get(email=email)
			if users.email == email and users.password == password:
				request.session['users_id'] = users.id
				return HttpResponseRedirect('/category_cat')
			else:
				return HttpResponseRedirect('/auth')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/auth')
	return render(
		request,
		'home/auth.html'
	)

def logout(request):
	try:
		del request.session['users_id']
	except KeyError:
		pass
	return render(
		request,
		'home/auth.html'
		)