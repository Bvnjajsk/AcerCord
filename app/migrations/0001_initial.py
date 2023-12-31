# Generated by Django 4.1.4 on 2023-05-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('telefono', models.CharField(max_length=45)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
    ]
