from django.db import models

# Create your models here.

class guest(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    address = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        