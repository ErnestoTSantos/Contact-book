# Generated by Django 4.2.7 on 2023-11-14 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_last_name'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInformation',
        ),
    ]
