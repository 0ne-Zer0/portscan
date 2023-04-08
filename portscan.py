#Importa biblioteca socket
import socket

#Lista de portas de conexão
port = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 53, 67, 68, 69 , 123, 137, 161, 500, 514, 520]

#Recebe o host alvo
host = input("Digite o host alvo: ")

#Laço teste de portas
for i in port:

    #Cria variável para fazer conexão
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Define timeout da conexão
    s.settimeout(1)

    #Fecha conexão com host e recebe código de resposta
    cod = s.connect_ex((host, i))

    #Mensagem de porta aberta
    if cod == 0:
        #Exibe resultado
        print(f"{i} ABERTA")
    else:
        print(f"{i} FECHADA")