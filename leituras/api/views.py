from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from leituras.models import Leitura
from leituras.api.serializers import LeituraSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_leituras(request):
    ll = Leitura.objects.all()
    lls = LeituraSerializer(ll, many=True)

    return Response(lls.data, status=status.HTTP_200_OK)
