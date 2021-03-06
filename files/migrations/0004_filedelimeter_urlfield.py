# Generated by Django 2.2.6 on 2019-10-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_file_file2'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDelimeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(upload_to='docs')),
            ],
        ),
        migrations.CreateModel(
            name='URLfield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]
