from django.db import models

# Create your models here.
class products(models.Model):
	name=models.CharField(max_length=50)
	weight=models.FloatField()
	created_at=models.DateField()
	updated_at=models.DateField()

	def __str__(self):
		return self.name
