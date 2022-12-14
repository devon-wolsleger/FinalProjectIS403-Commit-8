# Generated by Django 4.1.2 on 2022-12-13 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=50)),
                ('rent', models.IntegerField()),
            ],
            options={
                'db_table': 'Apartments',
            },
        ),
        migrations.CreateModel(
            name='Tennant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Person ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('rent_start', models.DateField()),
                ('rent_end', models.DateField()),
                ('appartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aptmanagement.apartments')),
            ],
            options={
                'db_table': 'Tennant',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Tennant ID')),
                ('admin', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='aptmanagement.tennant')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
    ]
