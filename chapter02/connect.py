import socket

if __name__ == "__main__" :
    ip = '127.0.0.1'
    port = 50000
    server = (ip, port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server)