import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5000))

print ("UDP server is up and listening on port 5000...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received {data.decode()} from {addr}")
        sock.sendto("Hi, I am UDP server".encode(), addr)
except KeyboardInterrupt:
    print("UDP server is shutting down...")
finally:
    sock.close()