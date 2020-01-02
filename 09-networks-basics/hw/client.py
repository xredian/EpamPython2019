import socket
import threading


def receive():
    """Receiving a message"""
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            print(message)
        except OSError:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1111))
thread = threading.Thread(target=receive).start()
msg = ''

while msg != 'quit':
    msg = input()
    client.send(bytes(msg, 'utf8'))

client.close()





