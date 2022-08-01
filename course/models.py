from django.db import models

# Create your models here.

class Course(models.Model):
#    id: int
#   price: int
#   offer = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    
