from django.db import models

# Create your models here.

class Post(models.Model):

	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	body = models.TextField(editable=False)

	

