import socket

ip = 'localhost'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('\nDigite a mensagem para enviar > ').encode('utf-8')
    client.sendto(msg, (ip, port))
    echo, serv = client.recvfrom(2048)
    print(f'Echo do server: {echo.decode("utf-8")}')
