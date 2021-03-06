# Generated by Django 3.0.8 on 2020-08-03 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('kawasaki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('kawasaki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kawasaki.Kawasaki')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
