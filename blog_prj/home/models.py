from django.db import models
from django import forms
from django.template.defaultfilters import slugify

class Tags(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=256)
	class Meta:
		db_table = 'tags'
		ordering = ['-id']
	def __str__(self):
		return self.name

class TagsForm(forms.ModelForm):
	name = forms.CharField(label='Name')
	class Meta:
		model = Tags
		fields = ['name']

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256,  default='')
    tags = models.ManyToManyField(Tags, related_name="tags_ids")
    summary = models.TextField(default= '')
    content = models.TextField(default= '')
    slug = models.SlugField(default='')

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return "/%s/" % (self.slug)

    def save(self):
        self.slug = slugify(self.title)
        super(Category,self).save()

    class Meta:
        db_table = "category"
        ordering = ['-id']

#form category
class CategoryForm(forms.ModelForm):
    title = forms.CharField(label='Title', min_length=3, max_length=100, strip=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    tags = models.ManyToManyField(Tags)
    summary = forms.CharField(label='Summary', widget = forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
    content = forms.CharField(label='Content', widget = forms.Textarea(attrs={'class':'form-control', 'rows':'20','id':'mytextarea',}))
    class Meta:
        model = Category
        fields = ['title', 'tags', 'summary', 'content']
        widgets = {
			'body': forms.Textarea(),
			'tags': forms.CheckboxSelectMultiple()
			}

# Create your models here.
class Users(models.Model):
	id = models.AutoField(primary_key=True)
	firt_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	role = models.CharField(max_length=256)
	email = models.CharField(max_length=256)
	class Meta:
		db_table = "users"
		ordering = ['-id']


#form user
class UsersForm(forms.ModelForm):
	firt_name = forms.CharField(label='Firt Name', max_length=100, strip=True)
	last_name = forms.CharField(label='Last Name', max_length=100, strip=True)
	password = forms.CharField(label='Password', max_length=100, strip=True)
	role = forms.CharField(label='Role', max_length=100, strip=True)
	email = forms.CharField(label='Email', max_length=100, strip=True)
	class Meta:
		model = Users
		fields = ['firt_name', 'last_name', 'password', 'role', 'email']