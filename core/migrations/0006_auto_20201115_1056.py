# Generated by Django 3.0 on 2020-11-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201115_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt',
            name='fees',
        ),
        migrations.AddField(
            model_name='debt',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
