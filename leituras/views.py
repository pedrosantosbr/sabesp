from django.shortcuts import render, redirect
from leituras.forms import UploadLeituraForm
from leituras.models import Folha, Leitura, Relatorio, RelatorioEvento
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required

from openpyxl import load_workbook


@login_required(login_url=settings.LOGIN_URL)
@transaction.atomic
def add_leitura(request):
    if request.method == "POST":
        form = UploadLeituraForm(request.POST, request.FILES)
        if form.is_valid():
            rl = Relatorio.objects.create()
            fl = Folha.objects.create(relatorio=rl, arquivo=request.FILES["file"])
            wb = load_workbook(request.FILES["file"])
            sheet = wb.active

            for row in sheet.iter_rows():
                Leitura.objects.create(
                    folha=fl,
                    rgi_principal=row[0].value,
                    rgi_autonoma=row[1].value,
                    status_valvula="Aberta",
                    data_leitura=row[5].value,
                    leitura=row[4].value,
                    fria_quente=row[3].value.split("-")[1],
                    imovel=row[2].value,
                    hidrometro="AZ000000",
                )

            RelatorioEvento.objects.create(
                funcionario=request.user,
                relatorio=rl,
                event_type=RelatorioEvento.EventTypes.CRIADO,
            )
            return redirect("dashboard")
    else:
        form = UploadLeituraForm()
    return render(request, "leituras/add.html", {"form": form})


@login_required(login_url=settings.LOGIN_URL)
@transaction.atomic
def edit_leitura(request, id):
    relatorio = get_object_or_404(Relatorio, pk=id)

    if request.method == "POST":
        form = UploadLeituraForm(request.POST, request.FILES)
        if form.is_valid():
            relatorio.folhas.all().delete()

            fl = Folha.objects.create(
                relatorio=relatorio, arquivo=request.FILES["file"]
            )
            wb = load_workbook(request.FILES["file"])
            sheet = wb.active

            for row in sheet.iter_rows():
                Leitura.objects.create(
                    folha=fl,
                    rgi_principal=row[0].value,
                    rgi_autonoma=row[1].value,
                    status_valvula="Aberta",
                    data_leitura=row[5].value,
                    leitura=row[4].value,
                    fria_quente=row[3].value.split("-")[1],
                    imovel=row[2].value,
                    hidrometro="AZ000000",
                )

            RelatorioEvento.objects.create(
                funcionario=request.user,
                relatorio=relatorio,
                event_type=RelatorioEvento.EventTypes.ATUALIZADO,
            )
            messages.success(request, "Leitura atualizada com sucesso!")
            return redirect("dashboard")
    else:
        form = UploadLeituraForm()

    return render(request, "leituras/edit.html", {"form": form, "relatorio": relatorio})


@login_required(login_url=settings.LOGIN_URL)
@transaction.atomic
def delete_relatorio(request, id):
    relatorio = get_object_or_404(Relatorio, pk=id)
    if request.method == "POST":
        relatorio.folhas.all().delete()
        relatorio.deleted_at = timezone.now()
        relatorio.save()

        messages.success(request, "Leitura deletada com sucesso!")

        return redirect("dashboard")
    return render(request, "leituras/delete.html", {"relatorio": relatorio})
