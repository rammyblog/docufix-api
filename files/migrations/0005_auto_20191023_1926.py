# Generated by Django 2.2.6 on 2019-10-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_filedelimeter_urlfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlfield',
            old_name='url',
            new_name='url1',
        ),
        migrations.AddField(
            model_name='urlfield',
            name='url2',
            field=models.URLField(default='http://'),
        ),
    ]
