from django.conf.urls import url
from blog import views as blog_views

urlpatterns = (
    url(r'^index', blog_views.index, name='index'),
	url(r'^success$', blog_views.success, name='success'),
	url(r'^update/(?P<id>[\d]+)$', blog_views.update_item, name='update'),
	url(r'^remove/(?P<id>[\d]+)$', blog_views.remove_item, name='remove'),
	url(r'^users$', blog_views.users, name='users'),

)