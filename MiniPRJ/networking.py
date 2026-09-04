import socket 
try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #for ipv6, use socket.AF_INET6 instead of socket.AF_INET
    #tcp protocol for SOCK_STREAM
    #udp protocol for SOCK_DGRAM
    
    sock.settimeout(3) #timeout for 3 seconds

    sock.connect(("g00gle.com", 443)) #port 443 for https
    #connection is made via 3wayhandshake
    print("Connection successful!")

except socket.error as e:
    print("Connection failed: ", e)

finally:
    sock.close()
