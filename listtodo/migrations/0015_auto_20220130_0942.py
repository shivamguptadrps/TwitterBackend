# Generated by Django 3.1.3 on 2022-01-30 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listtodo', '0014_auto_20220129_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='listtodo/static/img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweetedby',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
