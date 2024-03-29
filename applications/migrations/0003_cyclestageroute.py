# Generated by Django 4.0.5 on 2022-07-04 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_remove_application_current_statge_link_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CycleStageRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_stage_link_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='routes', to='applications.cycle_stage_link')),
                ('next_Cycle_stage_link_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nextroutes', to='applications.cycle_stage_link')),
            ],
        ),
    ]
