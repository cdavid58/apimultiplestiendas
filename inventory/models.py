from django.db import models
from company.models import Company

class Category(models.Model):
	name = models.CharField(max_length = 40, unique = True)
	img = models.ImageField(upload_to = "Categories",default = "null/foto.png")
	searched = models.IntegerField(max_length = 50, default = 0)

	def __str__(self):
		return self.name

class SubCategories(models.Model):
	name = models.CharField(max_length = 40)
	img = models.ImageField(upload_to = "SubCategory",default = "null/foto.png")
	category = models.ForeignKey(Category,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length = 100)
	price = models.FloatField()
	tax = models.FloatField(default = 0)
	quanty = models.FloatField(default = 1)
	description = models.TextField()
	shipping = models.FloatField(default = 0)
	company = models.ForeignKey(Company, on_delete= models.CASCADE)
	subcategories = models.ForeignKey(SubCategories, on_delete = models.CASCADE)
	img = models.ImageField(upload_to = "Inventory",default = "null/foto.png")
	more_sell = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

class Gallery(models.Model):
	img_1 = models.ImageField(upload_to = "Gallery", blank=True,null=True)
	img_2 = models.ImageField(upload_to = "Gallery", blank=True,null=True)
	img_3 = models.ImageField(upload_to = "Gallery", blank=True,null=True)
	img_4 = models.ImageField(upload_to = "Gallery", blank=True,null=True)
	img_5 = models.ImageField(upload_to = "Gallery", blank=True,null=True)
	product = models.ForeignKey(Product,on_delete = models.CASCADE)

class Features(models.Model):
	SIZE = [
		('ninguno','ninguno'),
		('xs',"xs"),
		('s','s'),
		('m','m'),
		('l','l'),
		('xl','xl'),
		('xxl','xxl'),
		('xxxl','xxxl')
	]
	STATE = (
		('Nuevo','Nuevo'),
		('Usado','Usado')
	)
	color = models.CharField(max_length = 30, blank=True,null=True)
	size = models.CharField(max_length = 10, choices= SIZE)
	state = models.CharField(max_length = 8, choices= STATE)
	marca = models.CharField(max_length = 40, blank=True,null=True)
	modelo = models.CharField(max_length = 40, blank=True,null=True)
	unidades_por_pack = models.IntegerField(default = 1)
	product = models.ForeignKey(Product,on_delete = models.CASCADE)

	def __str__(self):
		return self.product.name
