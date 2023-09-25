# Generated by Django 4.2.3 on 2023-09-25 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("leituras", "0002_remove_relatoriocriado_relatorioevento_ptr_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="folha",
            name="relatorio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="folhas",
                to="leituras.relatorio",
            ),
        ),
    ]
