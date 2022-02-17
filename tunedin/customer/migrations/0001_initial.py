# Generated by Django 4.0 on 2022-02-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_firstname', models.CharField(max_length=100)),
                ('customer_lastname', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=10)),
                ('customer_password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]