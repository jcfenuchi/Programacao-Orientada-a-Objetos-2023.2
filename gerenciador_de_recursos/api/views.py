from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HardwareInfo
from datetime import datetime
from django.shortcuts import render

@api_view(['GET'])
def getdata(request):
    meta_data = {
        'meta_data': HardwareInfo.objects.all()
    }
    return render(request, "dados/visualizar.html", meta_data)


@api_view(['POST'])
def addItem(request):
    hw = HardwareInfo()
    for k in request.data.keys():
        hostname = k
    hw.hostname = hostname
    
    hw.Host_ip = request.data.get(hostname).get("ip_client")

    # Parte da CPU
    hw.cpu_model = request.data.get(hostname).get("CPU").get('Model')
    hw.cpu_architecture = request.data.get(hostname).get("CPU").get('Architecture')
    hw.cpu_cores = request.data.get(hostname).get("CPU").get('Cores')
    hw.cpu_logical_cores = request.data.get(hostname).get("CPU").get('Logical Cores')
    hw.cpu_Frequency = request.data.get(hostname).get("CPU").get('Frequency')

    # Load Average Models
    hw.load_1min = request.data.get(hostname).get('Load Average').get('1 Minute')
    hw.load_5min = request.data.get(hostname).get('Load Average').get('5 Minutes')
    hw.load_15min = request.data.get(hostname).get('Load Average').get('15 Minutes')

    # Memory Models
    hw.memory_total = request.data.get(hostname).get('Memory').get("Total")
    hw.memory_available = request.data.get(hostname).get('Memory').get("Available")
    hw.memory_used = request.data.get(hostname).get('Memory').get('Used')
    hw.memory_percent = request.data.get(hostname).get('Memory').get('Percent')

    # Disk Usage Models
    hw.disk_total = request.data.get(hostname).get('Disk Usage').get('Total')
    hw.disk_free = request.data.get(hostname).get('Disk Usage').get('Free')
    hw.disk_used = request.data.get(hostname).get('Disk Usage').get('Used')
    hw.disk_percent = request.data.get(hostname).get('Disk Usage').get('Percent')

    # Boot Models
    hw.boot_time = request.data.get(hostname).get('Boot').get('Boot Time')
    hw.boot_uptime = request.data.get(hostname).get('Boot').get('Uptime')

    # Batery Models
    hw.batery_percent_charge = request.data.get(hostname).get('Battery').get('Percent Charge')
    hw.batery_power_is_plug = request.data.get(hostname).get('Battery').get('Power Plugged')

    # System Info Models
    hw.system_version = request.data.get(hostname).get('System Info').get('Version')
    hw.system_system_type = request.data.get(hostname).get('System Info').get('System')
    hw.system_distribution = request.data.get(hostname).get('System Info').get('Distribution')

    # Network Models
    hw.network_bytes_recv = request.data.get(hostname).get('Network').get('Bytes Received')
    hw.network_bytes_send = request.data.get(hostname).get('Network').get('Bytes Sent')

    hw.save()
    return Response({"status": 200})
