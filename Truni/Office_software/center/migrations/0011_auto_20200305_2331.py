# Generated by Django 3.0.4 on 2020-03-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0010_auto_20200305_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addurl_project_model',
            name='tenant_url',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
