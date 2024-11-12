from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    image = models.ImageField(upload_to='image')
    cost = models.PositiveIntegerField()
 
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True) 
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.user