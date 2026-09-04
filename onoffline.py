import socket
import time
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    sock.connect(("google.com", 443))
    print("Connected! You are online!")

except socket.error as e:
    time.sleep(1)
    print("You are offline!", e)

finally:
    sock.close()