# Generated by Django 2.1.15 on 2020-04-13 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salesreport',
            options={'ordering': ['fullname']},
        ),
    ]
