# Generated by Django 3.0.6 on 2020-06-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0154_auto_20200620_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='quota',
            name='release_after_exit',
            field=models.BooleanField(default=False),
        ),
    ]
