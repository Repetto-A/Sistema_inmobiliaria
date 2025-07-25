# Generated by Django 4.1.3 on 2023-04-26 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_inmobiliaria', '0014_alter_vendedor_apellido_alter_vendedor_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nombre', models.CharField(max_length=255)),
                ('cliente_apellido', models.CharField(max_length=255)),
                ('cliente_dni', models.CharField(max_length=8)),
                ('cliente_telefono', models.CharField(max_length=10)),
                ('cliente_domicilio', models.CharField(max_length=255)),
                ('cliente_email', models.EmailField(max_length=255)),
                ('monto', models.IntegerField()),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_inmobiliaria.propiedad')),
            ],
        ),
    ]
