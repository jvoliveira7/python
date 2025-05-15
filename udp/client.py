import socket
import threading

def receive_messages(sock):
    """Função para receber as mensagens do servidor em uma thread separada"""
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            print(f"\n📥 Mensagem recebida: {data.decode()}\n📤 Digite sua mensagem (ou 'sair'): ", end='')
        except:
            break

def start_client(host: str = 'localhost', port: int = 2000):
    """Inicia o cliente UDP"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Envia mensagem vazia para registrar no servidor
        client_socket.sendto(b"", (host, port))

        # Inicia thread para receber mensagens
        threading.Thread(
            target=receive_messages,
            args=(client_socket,),
            daemon=True
        ).start()
        
        print(f"✅ Conectado ao servidor UDP {host}:{port}")
        print("📤 Digite sua mensagem (ou 'sair'): ", end='')
        
        while True:
            message = input()
            client_socket.sendto(message.encode(), (host, port))
            
            if message.lower() == 'sair':
                break

if __name__ == '__main__':
    start_client()