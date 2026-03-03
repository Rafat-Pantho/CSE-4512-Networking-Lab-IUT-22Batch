import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
sock.settimeout(1.5)

messge = "Hail Hitler"
sock.sendto(messge.encode(),server_address)
try:
    data, _ = sock.recvfrom(1024)
    print(f"Received from server: {data.decode()}")
except socket.timeout:
    print("No response from server, timed out.")
finally:
    sock.close()