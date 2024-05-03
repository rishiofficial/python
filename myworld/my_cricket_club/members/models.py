from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    country = models.CharField(max_length = 240,null=True)
    joined_date = models.DateField(null=True)
    
def __str__(self):
    return f"{self.firstname} {self.lastname}"
# member6 = Member(firstname='shiva',lastname='parvati')
