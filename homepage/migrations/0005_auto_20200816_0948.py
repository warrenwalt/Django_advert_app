# Generated by Django 3.0.6 on 2020-08-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_subscribe_subscribe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]