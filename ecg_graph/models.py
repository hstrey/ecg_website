from django.db import models

# Create your models here.


class ECGdata(models.Model):
    data_json = models.TextField()
    created_date = models.DateTimeField('date created')
    models.ForeignKey('auth.User', related_name='ecg_data', on_delete=models.CASCADE)
