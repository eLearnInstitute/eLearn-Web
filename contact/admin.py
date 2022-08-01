from django.contrib import admin
from contact.models import Contact
# same as >>from .models import Contact
# Register your models here.
admin.site.register(Contact)
