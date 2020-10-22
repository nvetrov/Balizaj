# Generated by Django 3.0.7 on 2020-07-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bali_client', '0010_auto_20200712_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20, verbose_name='Номер отдела')),
            ],
            options={
                'verbose_name': 'Номер отдела',
                'verbose_name_plural': 'Номера отделов',
            },
        ),
    ]