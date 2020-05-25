from django.db import models

# Create your models here.
# its basically a DB stuff
# we are going to store only ticker or symbol of the stock in DB

# in Django, DB is a 2 step process
# 1. create a DataBase Model (this file)
# 2. Migrate the same (python manage.py makemigrations and after that python manage.py migrate in git BASH)

# after above add model in admin area


class stock(models.Model):
	ticker = models.CharField(max_length=10) # datatype is CharField

	def __str__(self): ## Admin area
		return self.ticker