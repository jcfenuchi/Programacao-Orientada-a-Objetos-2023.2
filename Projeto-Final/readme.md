### Servidor de Gerenciamento de Dados com suporte a bot do telegram.

#### como executar ? 
Maquina Servidor terminal 01:
```bash
cd gerenciador_de_recursos
python3 manager.py runserver
```

Maquina servidor terminal 02:
```bash
python3 echo_server.py
```

Maquinas cliente:
```bash
python3 sock_client.py 
# obs Alterar o ip para o da maquina servidora no codigo!.
```

Maquina telegram:
```bash
python3 telebot_run.py
# Alterar o ID do bot
```