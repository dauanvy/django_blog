from django.conf.urls import patterns, url
from upload import views as upload_views

urlpatterns = [
	url(
		r'^upload$',
		upload_views.upload,
		name='upload'),
	url(
	    r'^remove/(?P<id>[\d]+)$',
	    upload_views.remove_upload,
	    name='remove'),
]