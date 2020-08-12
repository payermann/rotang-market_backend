from django.db import models


class Product(models.Model):
    name = models.CharField("Наименование", max_length=255)
    price = models.IntegerField("Цена")
    specification = models.TextField("Описание", blank=True, null=True)
    image = models.ImageField("Картинка", null=True, blank=True)
    
    def __str__(self):
        return self.name
