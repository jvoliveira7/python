import socket

def start_client(host: str = 'localhost', port: int = 2000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"✅ Conectado ao servidor {host}:{port}")
        
        while True:
            message = input("📤 Digite sua mensagem (ou 'sair'): ")
            client_socket.sendall(message.encode())
            
            if message.lower() == 'sair':
                break
                
            response = client_socket.recv(1024).decode()
            print(f"📥 Servidor respondeu: {response}")

if __name__ == '__main__':
    start_client()