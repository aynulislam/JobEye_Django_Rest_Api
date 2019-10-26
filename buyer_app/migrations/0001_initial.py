# Generated by Django 2.2.6 on 2019-10-17 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(max_length=10, unique=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_node', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('voice', models.FileField(null=True, upload_to='')),
                ('face', models.FileField(null=True, upload_to='')),
                ('salt', models.IntegerField()),
                ('pin', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JeBuyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer_app.ScUser')),
            ],
        ),
    ]