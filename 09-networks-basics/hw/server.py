import socket
from threading import *


def accept_incoming_connections():
    """Sets up handling for incoming clients."""

    while True:
        client, client_address = server.accept()
        print(f'{client_address}:{client_address} has connected')
        client.send(bytes('Hi! Please, type your name and press enter: ',
                          'utf8'))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = f'Welcome {name}! If you ever want to quit, ' \
              f'type "^quit" to exit.\n' \
              f'If you want to get list of participants, type ^list.\n' \
              f'If you want to send private message,' \
              f' type ^!name of participant and your message.'
    client.send(bytes(welcome, "utf8"))
    msg = f'{name} has joined the chat'
    broadcast(bytes(msg, 'utf8'))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes('^quit', 'utf8'):
            client.send(bytes('^quit', 'utf8'))
            client.close()
            del clients[client]
            broadcast(bytes(f'{name} has left the chat', 'utf8'))
            break
        elif msg == bytes('^list', 'utf8'):
            participants(client)
        elif msg.startswith(bytes('^!', 'utf8')):
            private(client, msg)
        else:
            broadcast(msg, f'{name}: ')


def broadcast(msg, prefix=''):
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, 'utf8') + msg)


def participants(client):
    """Sending list of participants"""

    names = list(clients.values())
    participant = ', '.join(names)
    client.send(bytes(participant, 'utf8'))


def private(client, msg):
    """Sending private messages"""

    for recipient, name in clients.items():
        if msg.startswith(bytes(f'^!{name}', 'utf8')):
            message = f'Message from {clients[client]}:{str(msg[(len(name)+2):], "utf8")}'
            recipient.send(bytes(message, 'utf8'))


clients = {}
addresses = {}

IP_address = '0.0.0.0'
Port = 1111
BUFSIZ = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP_address, Port))

if __name__ == '__main__':
    server.listen(5)
    print('Waiting for connection...')
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.close()
