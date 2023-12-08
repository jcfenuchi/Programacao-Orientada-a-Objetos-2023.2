from django.db import models
from django.utils import timezone

# Create your models here.
class HardwareInfo(models.Model):
    index = models.AutoField(primary_key=True)
    hour_now = models.DateTimeField(default=timezone.now)
    # Host Name
    hostname = models.TextField(max_length=255)
    # Host IP
    Host_ip = models.TextField(max_length=40)

    # CPU Models
    cpu_model = models.TextField(max_length=100)
    cpu_architecture = models.TextField(max_length=25)
    cpu_cores = models.IntegerField()
    cpu_logical_cores = models.IntegerField()
    cpu_Frequency = models.TextField(max_length=30)

    # Load Average Models
    load_1min = models.IntegerField()
    load_5min = models.IntegerField()
    load_15min = models.IntegerField()

    # Memory Models
    memory_total = models.TextField(max_length=20)
    memory_available = models.TextField(max_length=20)
    memory_used = models.TextField(max_length=20)
    memory_percent = models.FloatField()

    # Disk Usage Models
    disk_total = models.TextField(max_length=20)
    disk_free = models.TextField(max_length=20)
    disk_used = models.TextField(max_length=20)
    disk_percent = models.FloatField()

    # Boot Models
    boot_time = models.DateTimeField()
    boot_uptime = models.TimeField()

    # Batery Models
    batery_percent_charge = models.FloatField()
    batery_power_is_plug = models.TextField(max_length=10)

    # System Info Models
    system_version = models.TextField(max_length=80)
    system_system_type = models.TextField(max_length=30)
    system_distribution = models.TextField(max_length=40)

    # Network Models
    network_bytes_recv = models.TextField(max_length=25)
    network_bytes_send = models.TextField(max_length=25)
