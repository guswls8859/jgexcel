# Generated by Django 2.0.13 on 2020-09-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]
