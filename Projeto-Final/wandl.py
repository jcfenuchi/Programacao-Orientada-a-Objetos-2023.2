import cpuinfo
import psutil
import platform
import os
import datetime
import distro
import time
from flask import Flask, jsonify


class Monitoring:
    def format_bytes(self, bytes):
        for unit in ['', 'KB', 'MB', 'GB', 'TB', 'PB']:
            if bytes < 1024.0:
                break
            bytes /= 1024.0
        return f"{bytes:.2f} {unit}"

    def format_seconds(self, seconds):
        return str(datetime.timedelta(seconds=seconds))

    def uptime(self):
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_hours = int(uptime_seconds // 3600)
        uptime_minutes = int((uptime_seconds % 3600) // 60)
        uptime_seconds = int(uptime_seconds % 60)
        return f"{uptime_hours:02d}:{uptime_minutes:02d}:{uptime_seconds:02d}"

    def get_system_info(self):
        # Obtém informações da CPU
        cpu_info = cpuinfo.get_cpu_info()
        cpu_freq = psutil.cpu_freq()

        # Verifica se a chave 'hz_advertised_raw' está presente
        frequency = cpu_info.get("hz_advertised_raw", "N/A")
        if frequency == "N/A":
            # Se não houver informações de frequência no psutil.cpu_info(), tenta obter do psutil.cpu_freq()
            frequency = f"{cpu_freq.current:.2f} MHz" if cpu_freq else "N/A"

        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
        system_uptime = self.uptime()

        try:
            battery = psutil.sensors_battery()
            percent_battery = battery.percent
            power_plugged = battery.power_plugged
        except AttributeError:
            percent_battery = "N/A"
            power_plugged = "N/A"

        network_info = psutil.net_io_counters()
        connections = psutil.net_connections(kind='inet')

        system_info = {
            "CPU": {
                "Model": cpu_info.get("brand_raw", "N/A"),
                "Architecture": platform.machine(),
                "Cores": psutil.cpu_count(logical=False),
                "Logical Cores": psutil.cpu_count(logical=True),
                "Frequency": frequency
            },
            "Load Average": {
                "1 Minute": os.getloadavg()[0],
                "5 Minutes": os.getloadavg()[1],
                "15 Minutes": os.getloadavg()[2]
            },
            "Memory": {
                "Total": self.format_bytes(psutil.virtual_memory().total),
                "Available": self.format_bytes(psutil.virtual_memory().available),
                "Used": self.format_bytes(psutil.virtual_memory().used),
                "Percent": psutil.virtual_memory().percent
            },
            "Disk Usage": {
                "Total": self.format_bytes(psutil.disk_usage('/').total),
                "Free": self.format_bytes(psutil.disk_usage('/').free),
                "Used": self.format_bytes(psutil.disk_usage('/').used),
                "Percent": psutil.disk_usage('/').percent
            },
            "Boot": {
                "Boot Time": str(boot_time),
                "Uptime": system_uptime,
            },
            "Battery": {
                "Percent Charge": percent_battery,
                "Power Plugged": "Yes" if power_plugged else "No"
            },
            "System Info": {
                "Version": platform.version(),
                "System": platform.system(),
                "Distribution": distro.id() if platform.system() == "Linux" else "N/A"
            },
            "Network": {
                "Bytes Received": self.format_bytes(network_info.bytes_recv),
                "Bytes Sent": self.format_bytes(network_info.bytes_sent)
            }
        }

        return system_info

    def api(self, port, ip="0.0.0.0"):
        app = Flask("__Monitor__")

        @app.route("/metrics_pc", methods=['GET'])
        def metric():
            return jsonify(self.get_system_info())

        return app.run(host=ip, port=port)


if __name__ == "__main__":
    mon = Monitoring()
    mon.api(port=7781)

    # Gera um arquivo JSON com as informações
    #with open("system_info.json", "w") as json_file:
    #    json.dump(system_info, json_file, indent=4)
    #print("Informações do sistema foram salvas em system_info.json.")
