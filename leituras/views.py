from django.shortcuts import render, redirect
from leituras.forms import UploadLeituraForm
from leituras.models import Folha, Leitura
from unidades.models import Unidade
from datetime import datetime

from openpyxl import load_workbook


def add_leitura(request):
    u = Unidade.objects.first()

    if request.method == "POST":
        form = UploadLeituraForm(request.POST, request.FILES)
        if form.is_valid():
            Folha.objects.create(arquivo=request.FILES["file"])
            wb = load_workbook(request.FILES["file"])
            sheet = wb.active
            for row in sheet.iter_rows():
                u = Unidade.objects.create(endereco=row[2].value)
                Leitura.objects.create(
                    unidade=u,
                    rgi_principal=row[0].value,
                    rgi_autonoma=row[1].value,
                    status_valvula="Aberta",
                    data_leitura=row[5].value,
                    leitura=row[4].value,
                    fria_quente=row[3].value.split("-")[1],
                    imovel=u.endereco,
                    hidrometro="AZ000000",
                )
            return redirect("dashboard")

    else:
        form = UploadLeituraForm()
    return render(request, "leituras/add.html", {"form": form, "unidade": u})
