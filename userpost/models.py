from django.db import models
# Create your models here.


class Postuser(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50,unique=True)
	password=models.CharField(max_length=20)
	username=models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.username


class PostData(models.Model):
	username=models.ForeignKey(Postuser,on_delete=models.CASCADE)
	text=models.TextField(max_length=50)
	created=models.DateField(auto_now_add=True)
	updated=models.DateField(auto_now=True)

	def __str__(self):
		return f'{self.username} posted {self.text}'
