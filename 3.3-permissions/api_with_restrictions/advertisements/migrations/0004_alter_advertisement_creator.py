# Generated by Django 4.0.4 on 2022-04-24 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0003_remove_advertisement_favourites_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisement', to=settings.AUTH_USER_MODEL),
        ),
    ]
