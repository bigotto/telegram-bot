#!/bin/bash
echo "Iniciando..."

# usuario = 'id -u'
# if [ "$usuario" != "0" ]
# then
#     echo -e "Usuário necessita ser root."
#     exit
# fi

# Verificar se possui pip instalado
apt-get install python-pip
# Instalar as libs necessarias
pip install speedtest-cli
pip install python-telegram-bot
