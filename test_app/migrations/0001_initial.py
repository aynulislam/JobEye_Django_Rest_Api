# Generated by Django 2.2.6 on 2019-10-20 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worker_app', '0001_initial'),
        ('general_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JeQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer_a', models.CharField(max_length=100)),
                ('answer_b', models.CharField(max_length=100)),
                ('answer_c', models.CharField(max_length=100)),
                ('answer_d', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=1)),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_app.JeSkill')),
            ],
        ),
        migrations.CreateModel(
            name='JeTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('test_marks', models.DecimalField(decimal_places=2, max_digits=4)),
                ('out_of', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker_app.JeWorker')),
            ],
        ),
        migrations.CreateModel(
            name='JeTestDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.JeQuestion')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.JeTest')),
            ],
        ),
    ]
