# Generated by Django 2.0 on 2019-01-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watsons', '0010_auto_20190106_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='delta_date',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]