from django.db import models

# Create your models here.

class Cpu(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    socket = models.IntegerField()
    frecuency = models.IntegerField()
    boost_frec = models.IntegerField()
    tdp = models.IntegerField()

class Ram_Memory(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    frecuency = models.IntegerField()
    memory_cl = models.IntegerField()

class Motherboard(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    chipset = models.CharField(max_length=20)
    socket = models.IntegerField()
    compatibility = models.CharField(max_length=20)