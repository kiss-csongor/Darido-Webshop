# Generated by Django 4.2.9 on 2024-02-25 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_message_valami_alter_message_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='content2',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='receiver2',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='sender2',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sent_date',
            new_name='sent_date2',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='valami',
            new_name='valami2',
        ),
    ]