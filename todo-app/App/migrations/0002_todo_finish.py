# Generated by Django 2.1.3 on 2019-04-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='finish',
            field=models.IntegerField(default=0),
        ),
    ]
