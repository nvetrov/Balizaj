# Generated by Django 3.0.7 on 2020-07-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bali_client', '0007_auto_20200707_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='other',
            name='material_type',
            field=models.CharField(default='Прочее', max_length=6, verbose_name='Прочее'),
        ),
        migrations.AddField(
            model_name='plasticholder',
            name='material_type',
            field=models.CharField(default='Пластиковый держатель', max_length=21, verbose_name='Пластиковый держатель'),
        ),
        migrations.AddField(
            model_name='pocket',
            name='material_type',
            field=models.CharField(default='Карман', max_length=6, verbose_name='Карман'),
        ),
        migrations.AddField(
            model_name='priceholder',
            name='material_type',
            field=models.CharField(default='Ценникодержатель', max_length=16, verbose_name='Ценникодержатель'),
        ),
        migrations.AddField(
            model_name='pricepaper',
            name='material_type',
            field=models.CharField(default='Бумага для ценников', max_length=19, verbose_name='Бумага для ценников'),
        ),
        migrations.AlterField(
            model_name='writeoffmaterial',
            name='department',
            field=models.CharField(default='Общий', max_length=10, verbose_name='Номер отдела'),
        ),
    ]