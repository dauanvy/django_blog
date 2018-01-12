# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from upload.models import Upload
from upload.models import UploadForm

# Create your views here.
def upload(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect('/upload/upload')
    else:
        img=UploadForm()
    images=Upload.objects.all()
    return render(request,'upload/upload.html',{'form':img,'images':images})

def remove_upload(request, id):
    data = {}
    try:
        selected_upload = Upload.objects.get(pk=id)
        selected_upload.delete()
        form = UploadForm()
    except Upload.DoesNotExist:
        raise Http404("This item not exist.")
    list_item = Upload.objects.all()
    data['id'] = None
    data['list_item'] = list_item
    data['form'] = form
    return HttpResponseRedirect('/upload/upload', data)