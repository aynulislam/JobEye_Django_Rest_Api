# Generated by Django 2.2.6 on 2019-10-20 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JeDurationUnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_unit_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JeJobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JeRateUnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_unit_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='JeSkillType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JeWorkStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JeSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=100)),
                ('categoty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_app.JeCategory')),
            ],
        ),
        migrations.CreateModel(
            name='JeSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('skill_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_app.JeSkillType')),
            ],
        ),
    ]
