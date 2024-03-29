from django.shortcuts import render
from leituras.models import Folha, Relatorio
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    user = request.user
    limit = request.GET.get("limit", 10)
    page_number = request.GET.get("page", 1)

    relatorios = (
        Relatorio.objects.prefetch_related("eventos").prefetch_related("folhas").all()
    )

    paginator = Paginator(relatorios, limit)

    page_obj = paginator.get_page(page_number)

    data = []

    for relatorio in page_obj:
        data.append(
            {
                "id": relatorio.id,
                "condominio": relatorio.condominio.nome,
                "folha": relatorio.folhas.first().arquivo.name.split("/")[-1],
                "created_at": relatorio.created_at.strftime("%d/%m/%Y %H:%M"),
                "deleted_at": relatorio.deleted_at.strftime("%d/%m/%Y %H:%M")
                if relatorio.deleted_at
                else None,
                "eventos": [
                    {
                        "id": evento.id,
                        "event_date": evento.event_date,
                        "funcionario": evento.funcionario.username,
                        "event_type": evento.event_type,
                    }
                    for evento in relatorio.eventos.all()
                ],
            }
        )

    return render(
        request,
        "dashboard/index.html",
        {"user": user, "relatorios": data, "page_obj": page_obj, "limit": limit},
    )
