from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from part.models import Cpu, Motherboard, RamMemory
# Create your views here.
def index(request):
    return render(request=request,
        context={},
        template_name='home/index.html',
    )
    
#Error en la busqueda hay que ajustar querys, por cuestiones de tiempo no llego a ajustarlo. No busca chipset, frecuencia y socket de forma individual.
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(model__contains=search_param)
        query.add(Q(brand__contains=search_param), Q.OR)
        cpu = Cpu.objects.filter(query)
        motherboard = Motherboard.objects.filter(query)
        rammemory = RamMemory.objects.filter(query)
        context_dict.update(
            {
                "cpus": cpu,
                "motherboards": motherboard,
                "rammemorys": rammemory,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/search_result.html",
    )