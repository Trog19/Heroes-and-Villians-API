from email.errors import CharsetError
from ssl import ALERT_DESCRIPTION_NO_RENEGOTIATION
from unicodedata import name
from urllib import request
from django.db import models
from django.forms import CharField
from super_types.models import SuperType

# Create your models here.


class Super(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    seccondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=100)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)