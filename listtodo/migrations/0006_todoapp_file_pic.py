# Generated by Django 3.2.10 on 2021-12-29 08:14

from django.db import migrations, models
import listtodo.models


class Migration(migrations.Migration):

    dependencies = [
        ('listtodo', '0005_remove_todoapp_file_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoapp',
            name='file_pic',
            field=models.ImageField(default=None, upload_to=listtodo.models.user_directory_path),
            preserve_default=False,
        ),
    ]
