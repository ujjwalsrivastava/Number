from django.db import models

class Number_store(models.Model):
    num=models.IntegerField()
    topic=models.CharField(max_length=30,default="LongWay")
    photo = models.ImageField(upload_to="gallery",null=True)
    class Meta:
        db_table='Number_store'

class Audio_storee(models.Model):
    record=models.FileField(upload_to='documents/')
    class Meta:
        db_table='Audio_store'
