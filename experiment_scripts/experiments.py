import matplotlib.pyplot as plt
import numpy as np
import math
import socket
import struct
import time
import control as ct

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

def gaussian_kernel_1d(length, sigma):
    ax = np.linspace(-(length - 1) / 2., (length - 1) / 2., length)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    return gauss / np.sum(gauss)

def main():
    results = []
    start_time = time.time()
    # while np.linalg.norm(state - start) > 1:
    for _ in range(200):
        start = np.array([-90.0, 0.0, 0.0, 0.0]) + np.random.normal(0, 0.5, 4)
        send_to_sock(start)
        state = recv_from_sock()

        error = state - start
        print(error)

        results.append([time.time() - start_time] + error.tolist())

    data = np.array(results)
    plt.plot(data[:, 0], data[:, 1], 'b-')
    plt.savefig("results.png")

    characteristics = ct.step_info(data[:, 1], data[:, 0], SettlingTimeThreshold=0.02) #

    # Extract the values
    settling_time = characteristics['SettlingTime']
    steady_state_value = characteristics['SteadyStateValue']
    steady_state_error = 0 - steady_state_value

    print(f"Steady State Value: {steady_state_value:.4f}")
    print(f"Steady State Error: {steady_state_error:.4f}")
    print(f"Settling Time (to within 2% of steady state): {settling_time:.4f} seconds")


if __name__ == '__main__':
    main()
