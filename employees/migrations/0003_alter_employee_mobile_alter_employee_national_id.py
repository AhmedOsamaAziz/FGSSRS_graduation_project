# Generated by Django 4.0.5 on 2022-07-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_email_employee_mobile_employee_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='national_id',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
