# Generated by Django 4.2.1 on 2023-06-04 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0031_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 4, 23, 27, 8, 987476, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]