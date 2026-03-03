import socket
import threading
import logging

logging.basicConfig(filename="server.log",level=logging.INFO, format="%(asctime)s - %(message)s")

sock = socket . socket ( socket . AF_INET , socket . SOCK_STREAM)

# Allow address reuse
sock . setsockopt ( socket . SOL_SOCKET , socket . SO_REUSEADDR , 1)

sock . bind (("0.0.0.0", 6006))
print (" UDP server listening on port 6006... ")

sock.listen()
clients=[]
# Handler for each incoming message
def handle_request ( client_sock, addr ) :
    logging.info(f"New connection from {addr}")
    clients.append(client_sock)
    try:
        while True:
            message = client_sock.recv(1024)
            if not message : break
            logging.info(f"Message from {addr}: {message}")
            for c in clients[:]:
                if c!=client_sock:
                    try:
                        c.send(message)
                    except:
                        clients.remove(c)

    except Exception as e:
        logging.error(f"Error : {e}")
    finally:
        print(f"{addr} disconnected")
        if client_sock in clients:
            clients.remove(client_sock)
        client_sock.close()

try:
    while True :
        client_sock , addr = sock . accept()
        # Spawn a new thread per request for concurrent handling
        # target specifies the callable ( function or method ) that the new thread will execute

        # A tuple of positional arguments to pass into target . In this case , once the thread begins , it effectively does :

        # daemon ensures threads wont prevent program exit

        threading . Thread ( target = handle_request , args =( client_sock, addr ) ,daemon = True ) . start ()
except KeyboardInterrupt :
    print ("\nShutting down server .")

# Islamic University of Technology (IUT)

sock . close ()