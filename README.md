# Portscan Simples em Python

Este é um pequeno projeto de portscan escrito em Python para fins de aprendizagem. Ele permite verificar quais portas estão abertas em um host específico e exibe o resultado na tela.

## Como usar
Faça o download do código-fonte ou clone este repositório em sua máquina.

- Abra um terminal na pasta do projeto e execute o seguinte comando:
python portscan.py

- Insira o endereço do host que você deseja escanear.

- O script iniciará o escaneamento das portas definidas no código e exibirá o resultado na tela.

## Como funciona
O script utiliza a biblioteca socket do Python para criar um socket e estabelecer uma conexão com o host. Em seguida, ele tenta se conectar em cada porta da lista de portas definida no código.

Se a porta estiver aberta, o script exibe a mensagem __"ABERTA"__. Caso contrário, exibe a mensagem __"FECHADA"__.

## Aviso
__O uso deste script é de inteira responsabilidade do usuário. Certifique-se de que está autorizado a escanear o host antes de executar o script. O autor não se responsabiliza pelo uso indevido do script.__
