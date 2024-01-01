# Generated by Django 5.0 on 2023-12-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notes",
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
                ("created", models.DateTimeField(auto_created=True)),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
            ],
        ),
    ]
