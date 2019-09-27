# Telegram Bot
> Script em Python no qual é possível enviar comandos através do Telegram Bot.

![image](https://user-images.githubusercontent.com/19173171/65646054-b9c9b200-dfc7-11e9-87ce-f0fc98f2bafa.png)


## Configuração:
1. Iniciar uma conversa com [@BotFather](https://telegram.me/BotFather)

2. Clique em Começar, e envie o comando _"/newbot"_

3. Defina o nome e um _username_

4. Copie o _token_ gerado

## Instalação no Raspberry(Raspbian):
1. Clonar o repositório

2. Subistuir _token_ em /src/main.py pelo gerado no BotFather:
    ```    
    updater = Updater('token')
    ```

3. Atribuir permissão de execução ao shell script:
    ```    
    $ chmod +x install.sh
    ```

4. Executar o script de instalação:
    ```    
    $ sudo ./install.sh
    ```

## Comandos Disponíveis:
* /speedtest: mede a velocidade da conexão à internet. 

## Novas funcionalidades:
Pode facilmente adicionadar novas funções no script /src/main.py