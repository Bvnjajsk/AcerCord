# Generated by Django 4.1.4 on 2023-05-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tortas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galletas',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=45)),
            ],
        ),
    ]