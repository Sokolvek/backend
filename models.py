from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    balance = models.IntegerField(null=True)
    email = models.CharField(max_length=45)

    class Meta:
        app_label = 'backend'

    def __str__(self):
        return self.username
    
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=45)
    product_description = models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    
    class Meta:
        app_label = 'backend'

    def __str__(self):
        return self.username