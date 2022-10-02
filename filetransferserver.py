import socket
import tqdm
import os
# device's IP address
SERVER_HOST = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5001
# Packet size of 4096 bytes
BUFFER_SIZE = 4096
#separator is formatting this so as long as it is the same in both files it works
SEPARATOR = " "
#instantiate socket. AF_INET what ip is it looking for. SOCK_STREAM stram data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
#opens the port to listen for clients trying to connect
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept() 
# confirmation the client connected
print(f"[+] {address} is connected.")
# receive the file information
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)
# start receiving the file from the socket
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()