import socket
import subprocess

def scan(ip):  print(f"Scanning {ip}...") for port in range(1, 100):     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)     result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")        sock.close()
target_ip= input("Enter the IP address to scan:")
scan(target_ip)