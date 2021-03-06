# Generated by Django 2.1.8 on 2019-05-26 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiBaseUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('symbol', models.CharField(blank=True, max_length=6, null=True)),
                ('dimension_symbol', models.CharField(blank=True, max_length=6, null=True)),
                ('quantity_name', models.CharField(blank=True, max_length=32, null=True)),
                ('value', models.FloatField(default=1.0)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='siunits_sibaseunit_related', related_query_name='siunits_sibaseunits', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='siunitss_sibaseunit_related', related_query_name='siunits_sibaseunits', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siunits.SiBaseUnit')),
            ],
            options={
                'verbose_name_plural': 'SI Base Units',
                'ordering': ('name',),
            },
        ),
    ]
