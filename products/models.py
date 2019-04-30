from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
	title   = models.CharField(max_length=50)
	desc    = models.TextField(null=True,blank=True)
	price   = models.DecimalField(max_digits=11110,decimal_places=2)
	summary = models.TextField(default='Great!')
	status  = models.BooleanField(default=True)

	
	def get_absolute_url_lookup(self):
	 	return reverse("dynamic-lookup",kwargs={'my_id':self.id})
	def get_absolute_url_edit(self):
		return  reverse("product-edit",kwargs={"my_id":self.id})
	def get_absolute_url_delete(self):
		return reverse("product-delete",kwargs={'my_id':self.id})
	def get_absolute_url_add(self):
	 	return reverse("add-product",kwargs={})
