# Generated by Django 3.0.4 on 2020-03-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_remove_registration_email_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='active_user',
        ),
        migrations.AlterField(
            model_name='registration',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
