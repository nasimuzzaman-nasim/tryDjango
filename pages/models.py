from django.db import models
from products.models import Product

# Create your models here.

class Pages(models.Model):
    title = models.charField(max_length=120)

   	def get_absolute_url_add():
		return reverse("add-product")
