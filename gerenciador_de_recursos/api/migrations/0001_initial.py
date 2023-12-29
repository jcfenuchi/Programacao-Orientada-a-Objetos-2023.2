# Generated by Django 4.2.6 on 2023-12-18 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HardwareInfo',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('hour_now', models.DateTimeField(default=django.utils.timezone.now)),
                ('hostname', models.TextField(max_length=255)),
                ('Host_ip', models.TextField(max_length=40)),
                ('cpu_model', models.TextField(max_length=100)),
                ('cpu_architecture', models.TextField(max_length=25)),
                ('cpu_cores', models.IntegerField()),
                ('cpu_logical_cores', models.IntegerField()),
                ('cpu_Frequency', models.TextField(max_length=30)),
                ('load_1min', models.IntegerField()),
                ('load_5min', models.IntegerField()),
                ('load_15min', models.IntegerField()),
                ('memory_total', models.TextField(max_length=20)),
                ('memory_available', models.TextField(max_length=20)),
                ('memory_used', models.TextField(max_length=20)),
                ('memory_percent', models.FloatField()),
                ('disk_total', models.TextField(max_length=20)),
                ('disk_free', models.TextField(max_length=20)),
                ('disk_used', models.TextField(max_length=20)),
                ('disk_percent', models.FloatField()),
                ('boot_time', models.DateTimeField()),
                ('boot_uptime', models.TextField(max_length=25)),
                ('batery_percent_charge', models.FloatField()),
                ('batery_power_is_plug', models.TextField(max_length=10)),
                ('system_version', models.TextField(max_length=80)),
                ('system_system_type', models.TextField(max_length=30)),
                ('system_distribution', models.TextField(max_length=40)),
                ('network_bytes_recv', models.TextField(max_length=25)),
                ('network_bytes_send', models.TextField(max_length=25)),
            ],
        ),
    ]
