from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=500, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True, default=1)

    def __str__(self):
        return self.title



