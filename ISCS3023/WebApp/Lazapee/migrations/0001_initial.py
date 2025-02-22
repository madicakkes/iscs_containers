# Generated by Django 5.0.1 on 2024-05-01 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=10)),
                ('rate', models.FloatField(max_length=300)),
                ('overtime_pay', models.FloatField(blank=True, null=True)),
                ('allowance', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('date_range', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('pay_cycle', models.IntegerField()),
                ('rate_cycle', models.FloatField()),
                ('earnings_allowance', models.FloatField()),
                ('deduction_tax', models.FloatField()),
                ('deduction_health', models.FloatField()),
                ('pag_ibig', models.FloatField()),
                ('sss', models.FloatField()),
                ('overtime', models.FloatField()),
                ('total_pay', models.FloatField()),
                ('id_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lazapee.employee')),
            ],
        ),
    ]
