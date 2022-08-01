from django.db import models

# Create your models here.


class Contact(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    ph_num = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=50)
    description = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
