import socket
import sys
import threading

target_IP = str(sys.argv[1])
target_port = int(sys.argv[2])

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg: break
            print(f"\n{msg.decode()}")
        except:break
    sock.close()

def send_message(sock):
    while True:
        try:
            usr_msg = input()
            if usr_msg =="/q":
                sock.close()
                break
            sock.send(usr_msg.encode())
        except:break

try:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect((target_IP,target_port))

    recv_thread = threading.Thread(target=receive_messages,args=(client_sock,),daemon=True)
    snd_thread = threading.Thread(target=send_message,args=(client_sock,),daemon=True)

    recv_thread.start()
    snd_thread.start()
    snd_thread.join()

except KeyboardInterrupt:
    print("done")
except Exception as e:
    print(f"Error: {e}")
finally:
    client_sock.close()