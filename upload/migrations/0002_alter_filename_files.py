# Generated by Django 4.0.2 on 2022-03-31 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filename',
            name='files',
            field=models.FileField(default=None, max_length=255, null=True, upload_to='media/file/'),
        ),
    ]
