# Generated by Django 4.2.10 on 2024-03-13 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='profile',
            new_name='sender',
        ),
    ]