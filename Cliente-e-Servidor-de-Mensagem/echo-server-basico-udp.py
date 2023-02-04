import socket

ip = 'localhost'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

while True:
   data, conn = server.recvfrom(2048)
   msg = data.decode("utf-8")
   print(f'Msg de: {conn}: {msg}')
   print('Echo a seguir...\n')
   server.sendto(data, conn)