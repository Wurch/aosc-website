# Generated by Django 3.1.5 on 2021-01-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='url',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project_url',
            field=models.URLField(default='none', help_text='The project repository URL'),
            preserve_default=False,
        ),
    ]
