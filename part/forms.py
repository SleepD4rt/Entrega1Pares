from django import forms

#Formulario para el microprocesador
class CpuForm(forms.Form):
    model = forms.CharField(
        label="Modelo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cpu-model",
                "placeholder": "modelo del procesador",
                "required": "True",
            }
        ),
    )
    brand = forms.CharField(
        label="Marca:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cpu-brand",
                "placeholder": "marca del procesador",
                "required": "True",
            }
        ),
    )
    socket = forms.CharField(
        label="Socket:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cpu-socket",
                "placeholder": "socket",
                "required": "True",
            }
        ),
    )
    frecuency = forms.FloatField(
        label="Frencuencia base:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cpu-frecuency",
                "placeholder": "en Ghz",
                "required": "True",
            }
        ),
    )
#Formulario para la RAM
class RamMemoryForm(forms.Form):
    model = forms.CharField(
        label="Modelo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "rammemory-model",
                "placeholder": "modelo de la memoria RAM",
                "required": "True",
            }
        ),
    )
    brand = forms.CharField(
        label="Marca:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "rammemory-brand",
                "placeholder": "marca de la memoria RAM",
                "required": "True",
            }
        ),
    )
    frecuency = forms.FloatField(
        label="Frencuencia:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cpu-frecuency",
                "placeholder": "en Mhz",
                "required": "True",
            }
        ),
    )
#Formulario de la Motherboard
class MotherboardForm(forms.Form):
    chipset = forms.CharField(
        label="Chipset:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "motherboard-chipset",
                "placeholder": "socket",
                "required": "True",
            }
        ),
    )
    model = forms.CharField(
        label="Modelo:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "motherboard-model",
                "placeholder": "modelo de la placa madre",
                "required": "True",
            }
        ),
    )
    brand = forms.CharField(
        label="Marca:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "motherboard-brand",
                "placeholder": "marca de la placa madre",
                "required": "True",
            }
        ),
    )
    socket = forms.CharField(
        label="Socket:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "motherboard-socket",
                "placeholder": "socket",
                "required": "True",
            }
        ),
    )
    
