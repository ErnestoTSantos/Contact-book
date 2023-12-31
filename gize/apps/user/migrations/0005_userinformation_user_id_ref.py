# Generated by Django 4.2.7 on 2023-11-17 03:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userinformation_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='user_id_ref',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
