# Generated by Django 3.2.8 on 2022-09-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0002_user_pswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='search_limit',
            field=models.IntegerField(default=0),
        ),
    ]
