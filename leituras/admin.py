from django.contrib import admin
from leituras.models import Leitura, Folha, Relatorio, RelatorioEvento

admin.site.register([Leitura, Folha, Relatorio, RelatorioEvento])
