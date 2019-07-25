# Generated by Django 2.1.8 on 2019-05-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]