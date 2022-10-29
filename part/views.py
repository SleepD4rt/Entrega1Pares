from django.shortcuts import render
from django.contrib import messages

from part.forms import CpuForm, MotherboardForm, RamMemoryForm
from part.models import Cpu, Motherboard, RamMemory
# Create your views here.
#CPU 
def create_cpus(request):
    if request.method == "POST":
        cpu_form = CpuForm(request.POST)
        if cpu_form.is_valid():
            data = cpu_form.cleaned_data
            actual_objects = Cpu.objects.filter(
                model=data["model"], brand=data["brand"], socket=data["socket"], frecuency=data["frecuency"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"El procesador {data['model']} - {data['brand']} ya está creado",
                )
            else:
                cpu = Cpu(model=data["model"], brand=data["brand"], socket=data["socket"], frecuency=data["frecuency"])
                cpu.save()
                messages.success(
                    request,
                    f"Procesador {data['model']} - {data['brand']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"cpus": Cpu.objects.all()},
                template_name="part/cpu_list.html",
            )

    cpu_form = CpuForm(request.POST)
    context_dict = {"form": cpu_form}
    return render(
        request=request,
        context=context_dict,
        template_name="part/cpu_form.html",
    )


def cpus(request):
    return render(
        request=request,
        context={"cpus": Cpu.objects.all()},
        template_name="part/cpu_list.html",
    )

#MOTHERBOARD

def create_motherboards(request):
    if request.method == "POST":
        motherboard_form = MotherboardForm(request.POST)
        if motherboard_form.is_valid():
            data = motherboard_form.cleaned_data
            actual_objects = Motherboard.objects.filter(
                chipset=data["chipset"], model=data["model"], brand=data["brand"], socket=data["socket"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"La placa madre {data['chipset']} - {data['model']} - {data['brand']} ya está creado",
                )
            else:
                motherboard = Motherboard(chipset=data["chipset"], model=data["model"], brand=data["brand"], socket=data["socket"])
                motherboard.save()
                messages.success(
                    request,
                    f"Placa madre {data['chipset']} - {data['model']} - {data['brand']} - {data['socket']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"motherboards": Motherboard.objects.all()},
                template_name="part/motherboard_list.html",
            )

    motherboard_form = MotherboardForm(request.POST)
    context_dict = {"form": motherboard_form}
    return render(
        request=request,
        context=context_dict,
        template_name="part/motherboard_form.html",
    )


def motherboards(request):
    return render(
        request=request,
        context={"motherboards": Motherboard.objects.all()},
        template_name="part/motherboard_list.html",
    )

#RAM_MEMORY

def create_rammemorys(request):
    if request.method == "POST":
        ramm_form = RamMemoryForm(request.POST)
        if ramm_form.is_valid():
            data = ramm_form.cleaned_data
            actual_objects = RamMemory.objects.filter(
                model=data["model"], brand=data["brand"], frecuency=data["frecuency"]
            ).count()
            if actual_objects:
                messages.error(
                    request,
                    f"El procesador {data['model']} - {data['brand']} ya está creado",
                )
            else:
                ramm = RamMemory(model=data["model"], brand=data["brand"], frecuency=data["frecuency"])
                ramm.save()
                messages.success(
                    request,
                    f"Memoria RAM {data['model']} - {data['brand']} - {data['frecuency']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"rammemorys": RamMemory.objects.all()},
                template_name="part/rammemory_list.html",
            )

    ramm_form = RamMemoryForm(request.POST)
    context_dict = {"form": ramm_form}
    return render(
        request=request,
        context=context_dict,
        template_name="part/rammemory_form.html",
    )


def rammemorys(request):
    return render(
        request=request,
        context={"rammemorys": RamMemory.objects.all()},
        template_name="part/rammemory_list.html",
    )