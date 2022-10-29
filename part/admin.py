from django.contrib import admin
from part.models import Cpu, Ram_Memory, Motherboard
# Register your models here.

admin.site.register(Cpu)
admin.site.register(Ram_Memory) 
admin.site.register(Motherboard)