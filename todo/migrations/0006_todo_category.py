# Generated by Django 3.1.4 on 2020-12-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201215_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.TextField(blank=True, null=True),
        ),
    ]