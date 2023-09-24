from django.shortcuts import render
from unidades.models import Unidade

from django.views.generic import ListView


class UnidadeListView(ListView):
    model = Unidade
    template_name = "unidades/index.html"
    context_object_name = "unidades"
    ordering = ["id"]
    paginate_by = 10


# Create your views here.
def list_unidades(request):
    unidades = Unidade.objects.all()
    return render(request, "unidades/index.html", {"unidades": unidades})
