from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username
    
class Category(models.Model):
    categoryname=models.CharField(max_length=200)
    imp=models.ImageField(upload_to='category')

    def __str__(self) -> str:
        return self.categoryname
    
class Product(models.Model):
    productcategory=models.ForeignKey(Category,on_delete=models.CASCADE)
    productname=models.CharField(max_length=200)
    productimage=models.ImageField(upload_to='product')
    productprice=models.IntegerField()
    productdescription=models.TextField()
    productquantity=models.IntegerField()
    def __str__(self) -> str:
        return self.productname