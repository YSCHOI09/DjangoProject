# Generated by Django 3.2.23 on 2023-12-07 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_userdata_today_feel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_ac', models.TextField(blank=True)),
                ('rec_fd', models.TextField(blank=True)),
                ('rec_pd', models.TextField(blank=True)),
                ('rec_ta', models.TextField(blank=True)),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.userdata')),
            ],
        ),
    ]
