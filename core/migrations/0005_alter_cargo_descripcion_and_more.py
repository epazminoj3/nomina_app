# Generated by Django 5.2.1 on 2025-05-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_rol_aniomes_alter_rol_bono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='rol',
            name='aniomes',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rol',
            name='bono',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rol',
            name='horas_extras',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rol',
            name='iess',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rol',
            name='neto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rol',
            name='sueldo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rol',
            name='tot_des',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rol',
            name='tot_ing',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tipocontrato',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
