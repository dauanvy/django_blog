from django.db import models
from django import forms
# Create your models here.

class Upload(models.Model):
    pic = models.ImageField("Image", upload_to="images/", default='')
    upload_date = models.DateTimeField(auto_now_add =True)
    class Meta:
        db_table = "upload_bl"
        ordering = ['-id']

# FileUpload form class.
class UploadForm(forms.ModelForm):
    pic = forms.ImageField(label='Select a file')
    class Meta:
        fields = ['pic']
        model = Upload
