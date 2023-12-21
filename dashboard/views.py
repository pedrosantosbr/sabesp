from django.shortcuts import render
from leituras.models import Folha, Relatorio
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    limit = request.GET.get("limit", 10)
    page_number = request.GET.get("page", 1)

    relatorios = Relatorio.objects.prefetch_related("eventos").all()

    paginator = Paginator(relatorios, limit)

    page_obj = paginator.get_page(page_number)

    print(paginator)
    data = []

    for relatorio in page_obj:
        data.append(
            {
                "id": relatorio.id,
                "condominio": relatorio.condominio.nome,
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
        {"relatorios": data, "page_obj": page_obj, "limit": limit},
    )
