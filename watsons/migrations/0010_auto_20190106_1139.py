# Generated by Django 2.0 on 2019-01-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watsons', '0009_transaction_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
