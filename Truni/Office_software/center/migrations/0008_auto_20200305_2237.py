# Generated by Django 3.0.4 on 2020-03-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0007_addurl_project_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addurl_project_model',
            name='Tenantid',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='addurl_project_model',
            name='tenant_url',
            field=models.URLField(),
        ),
    ]
