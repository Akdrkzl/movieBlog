# Generated by Django 4.2.7 on 2024-02-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0018_moviefavlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviefavlist',
            old_name='movie',
            new_name='favorite_movie',
        ),
    ]