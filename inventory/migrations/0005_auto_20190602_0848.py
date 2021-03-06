# Generated by Django 2.1.8 on 2019-06-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20190531_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='order_number',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='asset',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='serial_number',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
