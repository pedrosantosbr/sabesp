# Generated by Django 4.2.3 on 2023-09-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leituras", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="relatoriocriado",
            name="relatorioevento_ptr",
        ),
        migrations.RemoveField(
            model_name="relatoriodeletado",
            name="relatorioevento_ptr",
        ),
        migrations.AddField(
            model_name="relatorioevento",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("criado", "Criado"),
                    ("atualizado", "Atualizado"),
                    ("deletado", "Deletado"),
                ],
                default="criado",
                max_length=100,
            ),
        ),
        migrations.DeleteModel(
            name="RelatorioAtualizado",
        ),
        migrations.DeleteModel(
            name="RelatorioCriado",
        ),
        migrations.DeleteModel(
            name="RelatorioDeletado",
        ),
    ]