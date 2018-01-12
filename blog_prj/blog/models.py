from django.db import models
from django import forms

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    order = models.IntegerField()

    class Meta:
        db_table = "blog"
        ordering = ['-id']

#form category
class BlogForm(forms.ModelForm):
   title = forms.CharField(label='Title', min_length=3, max_length=100, strip=True)
   order = forms.IntegerField(label='Order', min_value=1)

   class Meta:
       model = Blog
       fields = ['title', 'order']

# Create your models here.
class BlogUsers(models.Model):
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=256, default='')
	password = models.CharField(max_length=256, default='')
	class Meta:
		db_table = "blogusers"
		ordering = ['-id']

#form user
class BlogUsersForm(forms.ModelForm):
	user_name = forms.CharField(label='User Name', max_length=100, strip=True)
	password = forms.CharField(label='Password', max_length=100, strip=True)
	class Meta:
		model = BlogUsers
		fields = ['user_name', 'password']