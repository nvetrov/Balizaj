# Generated by Django 3.0.6 on 2020-05-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bali_client', '0003_auto_20200509_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasticholderposition',
            name='position',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='plasticholdertype',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
