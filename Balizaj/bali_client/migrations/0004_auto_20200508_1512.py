# Generated by Django 3.0.6 on 2020-05-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bali_client', '0003_auto_20200508_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pocket',
            name='option',
            field=models.ForeignKey(default='без опций', null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketOption'),
        ),
    ]
