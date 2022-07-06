# Generated by Django 4.0.5 on 2022-07-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_student_person_id_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='national_id',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
