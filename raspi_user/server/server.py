import socket
import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

while True:
    try:
        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

        try:
            client_socket, address = s.accept()
        except KeyboardInterrupt as e:
            print(f"\nThe session has been terminated! Error: {e}")
            break

        print(f"[+] {address} is connected.")

        received = client_socket.recv(BUFFER_SIZE).decode()
        filename, filesize = received.split(SEPARATOR)

        filename = os.path.basename(filename)

        filesize = int(filesize)

        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            while True:
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break

                f.write(bytes_read)
                progress.update(len(bytes_read))
                print("\n")

    except Exception as e:
        print(f"The session has been terminated! Error: {e}")
        client_socket.close()
        s.close()
