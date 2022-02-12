from django.db import models

class Category_Shop(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='category_image', blank=False)
    discription = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='country', blank=False)

    def __str__(self):
        return self.title


class Category_Tanks(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(max_length=100)
    discription = models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.title

class Tanks(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category_Tanks, on_delete=models.CASCADE,null=True)
    img = models.ImageField(max_length=100)
    discription = models.TextField(max_length=1000,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Fuel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Tanks)
    img = models.ImageField(max_length=100,blank=True)
    discription = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

