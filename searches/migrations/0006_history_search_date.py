# Generated by Django 3.2.8 on 2022-09-22 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0005_auto_20220922_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='search_date',
            field=models.DateField(auto_now=True),
        ),
    ]