# Primeiro importamos as bibliotecas
import socket, struct

# Definição das variaveis para conexão
SERVER = '127.0.0.1'
PORT = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Definição do socket com o protocolo UDP
sock.settimeout(None) # Chamada do comando settimeout da API

s = 'sim'

# Criação do laço que pede o nome do arquivo para o cliente, faz o pedido ao servidor que depois envia o arquivo para o cliente
while s.lower() == 'sim':
    fileName = input("Arquivo a pedir ao servidor: ")
    print(f"Enviando pedido a {(SERVER, PORT)}.\nNome do arquivo: {fileName}")
    sock.sendto(fileName.encode('utf-8'), (SERVER, PORT))
    t, con = sock.recvfrom(512)
    s = struct.unpack('I', t)[0] # Gravação do tamanho do arquivo na variável s
    print(f'Tamanho do arquivo: {s} bytes')
    data, sour = sock.recvfrom(s) # Recebimento do arquivo com exatamente o tamanho dele em disponibilidade

    print("Gravando arquivo localmente a seguir...\n")
    with open(fileName, 'wb') as arq: # Criação e gravação do arquivo na máquina
        w = arq.write(data)
    s = input('Deseja continuar com pedidos? ')
    print('='*70)
sock.close() #fechamento do socket
