from django.db import models

# Create your models here.

class Faculties(models.Model):
#    id: int
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pic_fclty')
    desc = models.TextField()
    about = models.TextField()
    fb = models.CharField(max_length=50)
    ig = models.CharField(max_length=50)
    git = models.CharField(max_length=50)
    lnkd = models.CharField(max_length=50)
    twt = models.CharField(max_length=50)
    
