from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class HardwareInfo(models.Model):
    index = models.AutoField(primary_key=True)
    # Host Name
    hostname = models.TextField(max_length=255)
    # Host IP
    Host_ip = models.TextField(max_length=255)

    # CPU Models
    cpu_model = models.TextField(max_length=255)
    cpu_architecture = models.TextField(max_length=255)
    cpu_cores = models.IntegerField()
    cpu_logical_cores = models.IntegerField()
    cpu_Frequency = models.TextField(max_length=255)

    # Load Average Models
    load_1min = models.IntegerField()
    load_5min = models.IntegerField()
    load_15min = models.IntegerField()

    # Memory Models
    memory_total = models.TextField(max_length=255)
    memory_available = models.TextField(max_length=255)
    mamory_used = models.TextField(max_length=255)
    memory_percent = models.TextField(max_length=255)

    # Disk Usage Models
    disk_total = models.TextField(max_length=255)
    disk_free = models.TextField(max_length=255)
    disk_used = models.TextField(max_length=255)
    disk_percent = models.FloatField()

    # Boot Models
    boot_time = models.DateTimeField()
    boot_uptime = models.TimeField()

    # Batery Models
    batery_percent_charge = models.TextField(max_length=255)
    batery_power_is_plug = models.TextField(max_length=255)

    # System Info Models
    system_version = models.TextField(max_length=255)
    system_system_type = models.TextField(max_length=255)
    system_distribution = models.TextField(max_length=255)

    # Network Models
    network_bytes_recv = models.TextField(max_length=255)
    network_bytes_send = models.TextField(max_length=255)
