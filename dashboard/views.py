from django.shortcuts import render
from leituras.models import Folha
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    folhas = Folha.objects.all()
    return render(request, "dashboard/index.html", {"folhas": folhas})
