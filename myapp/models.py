import os

from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
from django_test import settings


class TestModel(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="test_images")
