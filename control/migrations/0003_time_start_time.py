# Generated by Django 2.2.3 on 2019-07-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='start_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]