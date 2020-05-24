# Generated by Django 3.0.6 on 2020-05-20 12:37

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
            options={
                'verbose_name': 'Складской адрес',
                'verbose_name_plural': 'Складские адреса',
            },
        ),
        migrations.CreateModel(
            name='OtherName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Прочее - полное наименование',
                'verbose_name_plural': 'Прочее - полные наименования',
            },
        ),
        migrations.CreateModel(
            name='OtherType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Прочее - тип (держатели, для стрелок, для профиля и т.д.)',
                'verbose_name_plural': 'Прочее - типы (держатели, для стрелок, для профиля и т.д.)',
            },
        ),
        migrations.CreateModel(
            name='PlasticHolderOrientation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(max_length=14)),
            ],
            options={
                'verbose_name': 'Ориентация пластикового держателя',
                'verbose_name_plural': 'Ориентация пластиковых держателей',
            },
        ),
        migrations.CreateModel(
            name='PlasticHolderPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Тип размещения пластикового держателя',
                'verbose_name_plural': 'Типы размещения пластикового держателя',
            },
        ),
        migrations.CreateModel(
            name='PlasticHolderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Тип пластикового держателя',
                'verbose_name_plural': 'Типы пластиковых держателей',
            },
        ),
        migrations.CreateModel(
            name='PocketFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Формат кармана',
                'verbose_name_plural': 'Форматы карманов',
            },
        ),
        migrations.CreateModel(
            name='PocketOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Дополнительные опции (доп. карманы, размеры доп. карманов, габариты)',
                'verbose_name_plural': 'Дополнительная опция (карман, размер и т.д.)',
            },
        ),
        migrations.CreateModel(
            name='PocketOrientation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation', models.CharField(max_length=14)),
            ],
            options={
                'verbose_name': 'Ориентация кармана',
                'verbose_name_plural': 'Ориентация карманов',
            },
        ),
        migrations.CreateModel(
            name='PocketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='PriceHolderFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Формат ценникодержателя (DBR20, DBR60 и т.д.)',
                'verbose_name_plural': 'Форматы ценникодержателей (DBR20, DBR60 и т.д.)',
            },
        ),
        migrations.CreateModel(
            name='PriceHolderHeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Высота ценникодержателя',
                'verbose_name_plural': 'Высота ценникодержателей',
            },
        ),
        migrations.CreateModel(
            name='PriceHolderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Тип ценникодержателя',
                'verbose_name_plural': 'Типы ценникодержателя',
            },
        ),
        migrations.CreateModel(
            name='PriceHolderWight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widht', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Ширина ценникодержателя',
                'verbose_name_plural': 'Ширина ценникодержателей',
            },
        ),
        migrations.CreateModel(
            name='PricePaperFormat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Формат бумаги для ценников (А2, А3 и т.д.)',
                'verbose_name_plural': 'Форматы бумаги для ценников (А2, А3 и т.д.)',
            },
        ),
        migrations.CreateModel(
            name='PricePaperType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Тип бумаги для ценников',
                'verbose_name_plural': 'Типы бумаги для ценников',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Номер магазина',
                'verbose_name_plural': 'Номера магазинов',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='SharedOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Address', verbose_name='Адрес на складе')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Shop', verbose_name='Магазин')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.Warehouse', verbose_name='Склад')),
            ],
        ),
        migrations.CreateModel(
            name='PricePaper',
            fields=[
                ('sharedoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bali_client.SharedOption')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Количество')),
                ('image', models.ImageField(blank=True, upload_to='images/pricepapers', verbose_name='Изображение')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PricePaperFormat', verbose_name='Формат')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PricePaperType', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Бумага для ценников',
                'verbose_name_plural': 'Бумага для ценников',
            },
            bases=('bali_client.sharedoption',),
        ),
        migrations.CreateModel(
            name='PriceHolder',
            fields=[
                ('sharedoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bali_client.SharedOption')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Количество')),
                ('image', models.ImageField(blank=True, upload_to='images/priceholders', verbose_name='Изображение')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PriceHolderFormat', verbose_name='Формат')),
                ('height', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PriceHolderHeight', verbose_name='Высота')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PriceHolderType', verbose_name='Тип')),
                ('wight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PriceHolderWight', verbose_name='Ширина')),
            ],
            options={
                'verbose_name': 'Ценникодержатель',
                'verbose_name_plural': 'Ценникодержатели',
            },
            bases=('bali_client.sharedoption',),
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('sharedoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bali_client.SharedOption')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Количество')),
                ('image', models.ImageField(blank=True, upload_to='images/pockets', verbose_name='Изображение')),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketFormat', verbose_name='Формат кармана')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketOption', verbose_name='Дополнительные опции')),
                ('orientation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketOrientation', verbose_name='Ориентация кармана')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PocketType', verbose_name='Тип кармана')),
            ],
            options={
                'verbose_name': 'Карман',
                'verbose_name_plural': 'Карманы',
            },
            bases=('bali_client.sharedoption',),
        ),
        migrations.CreateModel(
            name='PlasticHolder',
            fields=[
                ('sharedoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bali_client.SharedOption')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Количество')),
                ('image', models.ImageField(blank=True, upload_to='images/plasticholders', verbose_name='Изображение')),
                ('orientation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PlasticHolderOrientation', verbose_name='Ориентация')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PlasticHolderPosition', verbose_name='Размещение')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.PlasticHolderType', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Пластиковый держатель',
                'verbose_name_plural': 'Пластиковые держатели',
            },
            bases=('bali_client.sharedoption',),
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('sharedoption_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bali_client.SharedOption')),
                ('quantity', models.SmallIntegerField(default=0, verbose_name='Количество')),
                ('image', models.ImageField(blank=True, upload_to='images/others', verbose_name='Изображение')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.OtherName', verbose_name='Наименование')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bali_client.OtherType', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Прочее',
                'verbose_name_plural': 'Прочее',
            },
            bases=('bali_client.sharedoption',),
        ),
    ]