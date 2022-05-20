import socket
import tqdm
import os
import keygen
import picker

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = "{}".format(socket.gethostbyname(socket.gethostname()))
port = 8080

filename = f"./qf/{picker.newest()}"
filesize = os.path.getsize(filename)

s = socket.socket()

try:
    s.connect((host, port))
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
except:
    print("\nServer is unavailable, make sure the server is ready.")

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:

        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break

        try:
            s.sendall(bytes_read)
            progress.update(len(bytes_read))

        except:
            print("\nServer is being interrupted or intentionally closed.")
            break

s.close()
