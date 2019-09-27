!/bin/bash
echo "Iniciando..."

script_dir=`pwd`
echo "Diretório atual: $script_dir"

# Verificar se possui pip instalado
apt-get install python-pip
# Instalar as libs necessarias
pip install speedtest-cli
pip install python-telegram-bot

#Configura o serviço para iniciar automaticamente
#Backup
cp /etc/rc.local /etc/rc.local.bak
#Subistituindo
cp "$script_dir"/src/rc.local /etc/rc.local

echo "Concluido!"