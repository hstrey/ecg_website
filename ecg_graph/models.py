from django.db import models

# Create your models here.


class ECGdata(models.Model):
    data_json = models.CharField(max_length=1000)
    created_date = models.DateTimeField('date created')
