import socket
import tqdm
import os

SEPARATOR = " "
BUFFER_SIZE = 4096 # Packet size of 4096 bytes

# the ip address or hostname of the server, the receiver
host = "10.49.18.101"

port = 5001
# gets the name of file in the dir
filename = input("What is the name of the file you want to transfer? ")
# get the file size
filesize = os.path.getsize(filename)
#instantiate socket
s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()