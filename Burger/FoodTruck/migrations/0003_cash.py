# Generated by Django 2.1 on 2018-08-28 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodTruck', '0002_auto_20180827_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('sum_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
