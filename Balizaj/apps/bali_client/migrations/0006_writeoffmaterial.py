# Generated by Django 3.0.7 on 2020-07-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bali_client', '0005_auto_20200617_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteOffMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, verbose_name='Тип материала')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Количество')),
                ('name', models.CharField(max_length=80, verbose_name='Полное наименование материала')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время списания')),
                ('department', models.CharField(blank=True, max_length=10, verbose_name='Номер отдела')),
            ],
        ),
    ]