from rest_framework import serializers


class LeituraSerializer(serializers.Serializer):
    rgi_principal = serializers.CharField(max_length=20)
    rgi_autonoma = serializers.CharField(max_length=20)
    status_valvula = serializers.CharField(max_length=20)
    data_leitura = serializers.DateField()
    hora_leitura = serializers.TimeField()
    leitura = serializers.IntegerField()
    fria_quente = serializers.CharField(max_length=20)
    imovel = serializers.CharField(max_length=20)
    hidrometro = serializers.CharField(max_length=20)

    def to_representation(self, instance):
        # join date and time in a new var

        return {
            "rgiPrincipal": instance.rgi_principal,
            "rgiAutonoma": instance.rgi_autonoma,
            "statusValvula": instance.status_valvula,
            "dataLeitura": instance.data_leitura,
            "leitura": instance.leitura,
            "frioQuente": instance.tipo,
            "imovel": instance.imovel,
            "hidrometro": instance.hidrometro,
        }
