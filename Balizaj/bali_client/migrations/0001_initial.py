# Generated by Django 3.0.6 on 2020-05-08 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orientation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='PocketOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pockets', models.CharField(blank=True, max_length=10)),
                ('size', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='PocketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='images/pockets')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Address')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Format')),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketOption')),
                ('orientation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Orientation')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Shop')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketType')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Warehouse')),
            ],
        ),
    ]