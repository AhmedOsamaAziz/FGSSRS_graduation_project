# Generated by Django 4.0.5 on 2022-07-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_postponecoursedocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle_stage_link',
            name='is_init',
            field=models.BooleanField(default=False),
        ),
    ]