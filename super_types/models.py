from urllib import request
from django.db import models
from django.forms import CharField 
from super_types.apps import SuperTypesConfig

# Create your models here.


class SuperType(models.Model):
    type = CharField(max_length=50)