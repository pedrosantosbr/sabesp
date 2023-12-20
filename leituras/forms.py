from django import forms
from leituras.models import Leitura

COMPETENCIA_CHOICES = [
    ("JAN", "Janeiro"),
    ("FEV", "Fevereiro"),
    ("MAR", "Março"),
    ("ABR", "Abril"),
    ("MAI", "Maio"),
    ("JUN", "Junho"),
    ("JUL", "Julho"),
    ("AGO", "Agosto"),
    ("SET", "Setembro"),
    ("OUT", "Outubro"),
    ("NOV", "Novembro"),
    ("DEZ", "Dezembro"),
]


class UploadLeituraForm(forms.Form):
    # competencia = forms.ChoiceField(
    #     widget=forms.Select(
    #         attrs={
    #             "class": "shadow-dashboard appearance-none bg-gray-800 border border-gray-900 rounded-lg py-2 px-3 text-gray-200 leading-tight focus:outline-none focus:shadow-outline"
    #         }
    #     ),
    #     choices=COMPETENCIA_CHOICES,
    # )
    condominio_nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "shadow-dashboard appearance-none bg-gray-800 border border-gray-900 rounded-lg py-2 px-3 text-gray-200 leading-tight focus:outline-none focus:shadow-outline"
            }
        ),
        label="Nome do Condomínio",
    )
    file = forms.FileField(
        widget=forms.FileInput(attrs={"class": ""}),
        label="Arquivo",
    )
