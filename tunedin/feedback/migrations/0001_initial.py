# Generated by Django 4.0 on 2022-02-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=200)),
                ('need', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]