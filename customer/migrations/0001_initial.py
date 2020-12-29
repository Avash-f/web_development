# Generated by Django 3.0.8 on 2020-08-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]