# Generated by Django 5.0.6 on 2024-08-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_portfolio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cryptocurrency",
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
                ("name", models.CharField(max_length=100)),
                ("ticker", models.CharField(max_length=10, unique=True)),
                ("image", models.URLField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=8, max_digits=20)),
                ("market_cap", models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]