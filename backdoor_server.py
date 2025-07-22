import socket

server = socket.socket()
server.bind(("0.0.0.0", 4444))
server.listen(1)
print("[*] Listening for incoming connections...")

client, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    command = input("Shell> ")
    if command.lower() == "exit":
        client.send(b"exit")
        break
    client.send(command.encode())
    output = client.recv(1024).decode()
    print(output)
