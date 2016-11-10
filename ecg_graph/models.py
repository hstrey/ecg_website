from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ECGdata(models.Model):
    data_json = models.TextField()
    created_date = models.DateTimeField('date created')
    owner = models.ForeignKey(User, default=1)
