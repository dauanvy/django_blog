from django.conf.urls import patterns, url
from django.conf import settings
from home import views as home_views
from home.models import Category
from django.views.static import serve
from django.views.generic import ListView, DetailView
urlpatterns = patterns(
    '',
    url(
        r'^$',
        home_views.index,
        name='index'),
    url(
        r'^success$',
        home_views.success,
        name='success'),
    url(
        r'^category_cat$',
        home_views.category_cat,
        name='category_cat'),
	url(
	    r'^update_cat/(?P<id>[\d]+)$',
	    home_views.update_cat,
	    name='update_cat'),
	url(
	    r'^remove_cat/(?P<id>[\d]+)$',
	    home_views.remove_cat,
	    name='remove_cat'),
    url(
        r'^category_input$',
        home_views.category_input,
        name='category_input'),
    url(
		r'^tags$',
		home_views.tags,
		name='tags'),
	url(
		r'^update_tags/(?P<id>[\d]+)$',
		home_views.update_tags,
		name='update_tags'),
	url(
		r'^remove_tags/(?P<id>[\d]+)$',
		home_views.remove_tags,
		name='remove_tags'),

    url(
		r'^login$',
		home_views.login,
		name='login'),
	url(
		r'^auth$',
		home_views.auth,
		name='auth'),

	url(
		r'^update/(?P<id>[\d]+)$',
		home_views.update_item,
		name='update'),
	url(
		r'^remove/(?P<id>[\d]+)$',
		home_views.remove_item,
		name='remove'),
	url(
		r'^logout$',
		home_views.logout,
		name='logout'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(model=Category,),name='post'),
)