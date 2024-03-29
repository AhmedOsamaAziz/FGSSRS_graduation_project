# Generated by Django 4.0.5 on 2022-07-05 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_cyclestageroute'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostponeCourseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=150)),
                ('postpone_reason', models.TextField(max_length=255)),
                ('application_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='postponed_documents', to='applications.application')),
            ],
        ),
    ]
