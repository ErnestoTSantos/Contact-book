# Generated by Django 4.2.7 on 2023-11-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_id_ref',
            field=models.CharField(editable=False, max_length=50),
        ),
    ]
