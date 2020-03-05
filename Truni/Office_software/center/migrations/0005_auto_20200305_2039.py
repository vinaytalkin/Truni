# Generated by Django 3.0.4 on 2020-03-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0004_auto_20200305_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='employee_info',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=10),
        ),
    ]
