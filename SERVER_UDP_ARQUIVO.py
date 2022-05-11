#Primeiro importamos as bibliotecas
import socket, struct

#Definição das variaveis para conexão
INTERFACE = '127.0.0.1'
PORT = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Definição do socket com o protocolo UDP
sock.bind((INTERFACE, PORT)) # Estabelecimento da INTERFACE local com o IP e PORTA

print("Escutando em ...", (INTERFACE, PORT))
sock.settimeout(None) # Chamada do comando settimeout da API

# Criação do laço que recebe o nome do arquivo do cliente e depois envia o arquivo para o cliente
while True:
    print('='*70)
    print('Aguardando Cliente...')
    data, source = sock.recvfrom(512) # Recebimento do pacote do cliente
    fileName = data.decode('utf-8')
    print(f"Recebi pedido de: {source}.\nArquivo pedido: {fileName}")

    # Abertura do arquivo pedido pelo cliente
    with open(fileName, 'rb') as arq:
        ler = arq.read()
        print(f"Tamanho do arquivo: {len(ler)} bytes.") # Leitura do tamanho do arquivo
        s = struct.pack('I', len(ler))
        sock.sendto(s, source) # Envio do tamanho do arquivo
        pos = 0
        print(f"Enviando arquivo {fileName} a seguir...") # Envio do arquivo para o cliente
        while len(ler) > pos:
            env = sock.sendto(ler[pos:pos+4096], source)
            pos += int(env)

sock.close()
