# Generated by Django 4.2.3 on 2024-01-23 14:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("leituras", "0003_alter_condominio_nome"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="folha",
            options={"ordering": ["-created_at"]},
        ),
    ]