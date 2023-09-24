# Generated by Django 4.2.3 on 2023-08-28 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("unidades", "0002_remove_unidade_nome"),
        ("leituras", "0002_remove_leitura_competencia_remove_leitura_unidade"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="folha",
            name="leitura",
        ),
        migrations.RemoveField(
            model_name="leitura",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="leitura",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="leitura",
            name="unidade",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="unidades.unidade",
            ),
            preserve_default=False,
        ),
    ]
