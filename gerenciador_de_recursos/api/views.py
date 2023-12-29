from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HardwareInfo
from django.db.models import Max
from django.utils import timezone
from django.http import JsonResponse
from django.utils.html import escape
from django.shortcuts import render

@api_view(['GET'])
def home(request):
    # Obtém o parâmetro de consulta 'hostname' da URL
    hostname = request.GET.get('hostname', '')

    # Consulta para obter as informações mais recentes sobre o host fornecido
    informacoes_host = (
        HardwareInfo.objects
        .filter(hostname=hostname)
        .order_by('-hour_now')  # Ordena pela data mais recente
        .first()  # Limita a consulta para obter apenas o primeiro registro
    )

    if informacoes_host:
        # Formatar a data e hora no formato pt-BR
        data_hora_formatada = informacoes_host.hour_now.astimezone(timezone.get_default_timezone()).strftime('%d/%m/%Y %H:%M:%S')

        # Adiciona a data formatada ao objeto informacoes_host
        informacoes_host.hour_now_formatted = data_hora_formatada

        # Renderiza o template com as informações
        return render(request, 'dados/informacoes_host_template.html', {'informacoes_host': informacoes_host})
    else:
        return JsonResponse({'404': 'Host não encontrado'}, status=404)


@api_view(['GET'])
def last_minutes_hostname(request):
    # Consulta para obter os últimos hostnames nos últimos 5 minutos
    agora = timezone.now()
    cinco_minutos_atras = agora - timezone.timedelta(minutes=30)
    hostnames_recentes = (
        HardwareInfo.objects
        .filter(hour_now__gte=cinco_minutos_atras)
        .values('hostname')
        .annotate(ultima_data=Max('hour_now'))
        .order_by('-ultima_data')
    )
    # Converte a queryset para uma lista
    hostnames_lista = list(hostnames_recentes)
    return JsonResponse({'hostnames_recentes': hostnames_lista}, safe=False)


@api_view(['GET'])
def getdata(request):
    # Obtém o parâmetro de consulta 'hostname' da URL
    hostname = request.GET.get('hostname', '')

    # Consulta para obter as informações mais recentes sobre o host fornecido
    informacoes_host = (
        HardwareInfo.objects
        .filter(hostname=hostname)
        .order_by('-hour_now')  # Ordena pela data mais recente
        .first()  # Limita a consulta para obter apenas o primeiro registro
    )

    if informacoes_host:
        # Criar uma mensagem formatada em HTML para o Telegram
        data_hora_formatada = informacoes_host.hour_now.astimezone(timezone.get_default_timezone()).strftime('%d/%m/%Y %H:%M:%S')

        informacoes_html = (
            f"<b>🖥️ Hostname:</b> {informacoes_host.hostname}\n"
            f"<b>🕒 Última Atualização:</b> {data_hora_formatada}\n"
            f"<b>💻 CPU Model:</b> {informacoes_host.cpu_model}\n"
            f"<b>🔢 CPU Architecture:</b> {informacoes_host.cpu_architecture}\n"
            f"<b>🧠 CPU Cores:</b> {informacoes_host.cpu_cores}\n"
            f"<b>💽 CPU Logical Cores:</b> {informacoes_host.cpu_logical_cores}\n"
            f"<b>💽 CPU Frequency:</b> {informacoes_host.cpu_Frequency}\n"
            f"<b>🔄 Load Average (1min):</b> {informacoes_host.load_1min}\n"
            f"<b>🔄 Load Average (5min):</b> {informacoes_host.load_5min}\n"
            f"<b>🔄 Load Average (15min):</b> {informacoes_host.load_15min}\n"
            f"<b>💾 Memory Total:</b> {informacoes_host.memory_total}\n"
            f"<b>💽 Memory Available:</b> {informacoes_host.memory_available}\n"
            f"<b>🧠 Memory Used:</b> {informacoes_host.memory_used}\n"
            f"<b>💾 Memory Percent:</b> {informacoes_host.memory_percent}%\n"
            f"<b>💽 Disk Total:</b> {informacoes_host.disk_total}\n"
            f"<b>💾 Disk Free:</b> {informacoes_host.disk_free}\n"
            f"<b>🧠 Disk Used:</b> {informacoes_host.disk_used}\n"
            f"<b>💾 Disk Percent:</b> {informacoes_host.disk_percent}%\n"
            f"<b>🚀 Boot Time:</b> {informacoes_host.boot_time}\n"
            f"<b>⏲️ Boot Uptime:</b> {informacoes_host.boot_uptime}\n"
            f"<b>🔋 Battery Percent Charge:</b> {informacoes_host.batery_percent_charge}%\n"
            f"<b>🔌 Battery Power Is Plug:</b> {informacoes_host.batery_power_is_plug}\n"
            f"<b>🖥️ System Version:</b> {informacoes_host.system_version}\n"
            f"<b>🖥️ System System Type:</b> {informacoes_host.system_system_type}\n"
            f"<b>🖥️ System Distribution:</b> {informacoes_host.system_distribution}\n"
            f"<b>📈 Network Bytes Received:</b> {informacoes_host.network_bytes_recv}\n"
            f"<b>📉 Network Bytes Sent:</b> {informacoes_host.network_bytes_send}\n"
        )
        return JsonResponse({'200': informacoes_html}, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'404': 'Host nao encontrado'}, status=404)

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
