# Generated by Django 4.1.7 on 2023-06-01 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0026_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 1, 10, 22, 55, 349705, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]