# Generated by Django 4.1.4 on 2023-01-02 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_clickeventmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClickEventManager',
        ),
    ]