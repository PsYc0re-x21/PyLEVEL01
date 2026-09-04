import socket

try:
    ip = socket.gethostbyname("facwsdeb00k.com")
    print(ip)

except socket.gaierror as e:
    print("Hostname not found: ", e)
     