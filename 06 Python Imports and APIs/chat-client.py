
# chat-client.py - supplied by Cluade.ai
import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 12345

'''
use_localhost = input("Use localhost? (y/n): ").lower() == 'y'
HOST = '127.0.0.1' if use_localhost else input("Enter server IP address: ")
'''


my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:
    message = input(f'{my_username} > ')
    
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            
            print(f'{username} > {message}')
    
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error:', str(e))
            sys.exit()
        continue
    
    except Exception as e:
        print('General error:', str(e))
        sys.exit()


# If you are able to connect to devices on the same network... or via the internet 
# You'll need to figure out the IP of the server device - 'ipconfig' for Windows, or 'ifconfig' for Mac/Linux
# Furthermore, check the port you're using is open in the firewall...  


'''' 
import socket
import select
import errno
import sys

HEADER_LENGTH = 10
PORT = 12345

# Prompt for server IP
server_ip = input("Enter server IP address: ")

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

print(f"Connected to server at {server_ip}:{PORT}")

while True:
    message = input(f'{my_username} > ')
    
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)
    
    try:
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')
            
            print(f'{username} > {message}')
    
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error:', str(e))
            sys.exit()
        continue
    
    except Exception as e:
        print('General error:', str(e))
        sys.exit()

'''