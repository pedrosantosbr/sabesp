# Generated by Django 4.2.3 on 2024-01-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leituras", "0004_alter_folha_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leitura",
            name="hora_leitura",
        ),
        migrations.AlterField(
            model_name="leitura",
            name="data_leitura",
            field=models.DateTimeField(),
        ),
    ]