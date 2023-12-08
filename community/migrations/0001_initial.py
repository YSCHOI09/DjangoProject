# Generated by Django 4.2.7 on 2023-12-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodayContent",
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
                ("todaycontent", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="UserData",
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
                ("height", models.CharField(max_length=50)),
                ("weight", models.CharField(max_length=50)),
                ("action_lv", models.CharField(max_length=50)),
                ("action_cl", models.CharField(max_length=50)),
                ("action_pp", models.CharField(max_length=50)),
                ("action_tm", models.CharField(max_length=50)),
                ("action_wk", models.CharField(max_length=50)),
                ("action_pc", models.CharField(max_length=50)),
                ("health", models.CharField(max_length=200)),
            ],
        ),
    ]
