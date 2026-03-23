import numpy as np
import socket
import struct
import time

mechanism_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mechanism_socket.bind(('127.0.0.1', 8887))

# 3. Start listening for incoming connections
mechanism_socket.listen()
print("Server started at 127.0.0.1:8887...")

mechanism_conn, mechanism_addr = mechanism_socket.accept()
print(f"Connection received from address: {mechanism_addr}")

def send_to_sock(data):
    assert len(data) == 4
    package = struct.pack("<4f", *data)
    mechanism_conn.send(package)

def recv_from_sock():
    package = b""
    while len(package) < 16:
        package += mechanism_conn.recv(16 - len(package))

    result = np.array(struct.unpack("<4f", package))
    return result

start = np.array([0.0, 0.0, 90.0, 0.0])
send_to_sock(start)
state = recv_from_sock()

results = []
while np.linalg.norm(state - start) > 1:
    state = recv_from_sock()

    print(state)
    results.append(state - start)

time.sleep(10)
