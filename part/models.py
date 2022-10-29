from django.db import models

# Create your models here.

class Cpu(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    socket = models.CharField(max_length=10)
    frecuency = models.FloatField()
    #boost_frec = models.IntegerField()
    #tdp = models.IntegerField()

class RamMemory(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    frecuency = models.FloatField()
    #memory_cl = models.IntegerField()

class Motherboard(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    chipset = models.CharField(max_length=20)
    socket = models.CharField(max_length=20)
    #compatibility = models.CharField(max_length=20)