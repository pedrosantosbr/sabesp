from django.shortcuts import render
from leituras.models import Folha, Relatorio
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    relatorios = Relatorio.objects.prefetch_related("eventos").all()

    data = []

    for relatorio in relatorios:
        data.append(
            {
                "id": relatorio.id,
                "created_at": relatorio.created_at.strftime("%d/%m/%Y %H:%M"),
                "deleted_at": relatorio.deleted_at.strftime("%d/%m/%Y %H:%M")
                if relatorio.deleted_at
                else None,
                "eventos": [
                    {
                        "id": evento.id,
                        "event_date": evento.event_date.strftime("%d/%m/%Y %H:%M"),
                        "funcionario": evento.funcionario.username,
                        "event_type": evento.event_type,
                    }
                    for evento in relatorio.eventos.all()
                ],
            }
        )

    return render(request, "dashboard/index.html", {"relatorios": data})
