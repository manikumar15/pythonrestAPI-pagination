from django.db import models

class Emp(models.Model):
	empid=models.IntegerField(primary_key=True)
	empname=models.CharField(max_length=20)
	email=models.EmailField(max_length=30)
	salary=models.IntegerField()

	def __str__(self):
		return self.empname
