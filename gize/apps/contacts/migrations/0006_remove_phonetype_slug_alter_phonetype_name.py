# Generated by Django 4.2.7 on 2023-11-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_alter_contact_user_id_ref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonetype',
            name='slug',
        ),
        migrations.AlterField(
            model_name='phonetype',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
