from django.urls import path, include 

from part import views

app_name = "part"
urlpatterns = [
    path("cpus", view=views.cpus, name="cpu-list"),
    path("cpu/add", view=views.create_cpus, name="cpu-add"),
    path("motherboards", view=views.motherboards, name="motherboard-list"),
    path("motherboard/add", view=views.create_motherboards, name="motherboard-add"),
    path("rammemorys", view=views.rammemorys, name="rammemory-list"),
    path("rammemory/add", view=views.create_rammemorys, name="rammemory-add"),
]