# Generated by Django 4.2.7 on 2023-11-15 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_userinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
    ]
