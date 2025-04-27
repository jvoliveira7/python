import socket

def start_server(host: str = 'localhost', port: int = 2000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"🚀 Servidor escutando em {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"🔌 Conexão estabelecida com {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data or data.lower() == 'sair':
                    break
                print(f"📩 Cliente disse: {data}")
                conn.sendall(f"ECHO: {data}".encode())

if __name__ == '__main__':
    start_server()

    