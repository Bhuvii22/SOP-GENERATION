# Generated by Django 4.2.4 on 2023-09-04 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=15)),
                ('highest_education', models.CharField(max_length=40)),
                ('institute', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=20)),
                ('work_exp', models.CharField(max_length=100, null=True)),
                ('inscanada', models.CharField(max_length=100, null=True)),
                ('POS', models.CharField(max_length=50, null=True)),
                ('feepaid', models.CharField(max_length=50, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('completed_gic', models.CharField(max_length=10, null=True)),
                ('gicamount', models.IntegerField(null=True)),
                ('read', models.IntegerField(null=True)),
                ('write', models.IntegerField(null=True)),
                ('speak', models.IntegerField(null=True)),
                ('listen', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
    ]