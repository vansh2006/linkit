# Generated by Django 4.1.4 on 2022-12-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_shorturl_shortcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURLManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
