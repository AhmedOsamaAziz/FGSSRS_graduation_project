# Generated by Django 4.0.5 on 2022-07-01 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0002_remove_person_person_id'),
        ('students', '0002_remove_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='overall_rating',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='person_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='generic.person'),
            preserve_default=False,
        ),
    ]