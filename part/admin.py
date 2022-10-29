from django.contrib import admin
from part.models import Cpu, RamMemory, Motherboard
# Register your models here.

admin.site.register(Cpu)
admin.site.register(RamMemory) 
admin.site.register(Motherboard)