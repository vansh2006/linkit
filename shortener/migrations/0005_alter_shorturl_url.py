# Generated by Django 4.1.4 on 2022-12-31 19:12

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_delete_shorturlmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url]),
        ),
    ]
