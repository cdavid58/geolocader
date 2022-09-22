# Generated by Django 3.2.8 on 2022-09-22 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locate', '0003_user_search_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=25)),
                ('redirect', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locate.user')),
            ],
        ),
    ]
