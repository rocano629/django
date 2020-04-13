# Generated by Django 2.1.15 on 2020-04-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salespersonid', models.IntegerField(blank=True, null=True)),
                ('fullname', models.CharField(blank=True, max_length=152, null=True)),
                ('jobtitle', models.CharField(max_length=50, null=True)),
                ('salesterritory', models.CharField(max_length=50, null=True)),
                ('number_2011', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('number_2012', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('number_2013', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('number_2014', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'ordering': ['fullname'],
            },
        ),
    ]
