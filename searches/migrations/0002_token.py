# Generated by Django 3.2.8 on 2022-09-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=96)),
            ],
        ),
    ]
