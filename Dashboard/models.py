from django.db import models

# Create your models here.

class Dashboard(models.Model):

    highlight = models.TextField()
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='docs_img')
    desc = models.TextField()

