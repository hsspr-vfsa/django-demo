# Generated by Django 4.2.3 on 2023-07-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bank_name", models.CharField(max_length=100)),
                ("account_id", models.IntegerField()),
                ("tr_id", models.IntegerField()),
            ],
        ),
    ]
