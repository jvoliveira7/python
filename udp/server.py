import socket
from typing import Set, Tuple

class UDPServer:
    def __init__(self, host: str = 'localhost', port: int = 2000):
        """Inicializa o servidor UDP"""
        self.clients: Set[Tuple[str, int]] = set()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        print(f"🚀 Servidor UDP escutando em {host}:{port}")

    def broadcast(self, message: bytes, sender: Tuple[str, int]):
        """Envia mensagem para todos os clientes exceto o remetente"""
        for client in self.clients:
            if client != sender:
                try:
                    self.socket.sendto(message, client)
                except Exception as e:
                    print(f"⚠️ Erro ao enviar para {client}: {e}")
                    self.clients.discard(client)

    def run(self):
        """Executa o loop principal do servidor"""
        while True:
            try:
                data, addr = self.socket.recvfrom(1024)
                
                # Verifica se é uma mensagem de registro (vazia)
                if not data:
                    if addr not in self.clients:
                        print(f"🔌 Novo cliente conectado: {addr}")
                        self.clients.add(addr)
                    continue
                
                # Adiciona novo cliente se não estiver na lista
                if addr not in self.clients:
                    print(f"🔌 Novo cliente conectado: {addr}")
                    self.clients.add(addr)
                
                # Processa mensagem "sair"
                if data.decode().lower() == 'sair':
                    print(f"🚪 Cliente desconectado: {addr}")
                    self.clients.discard(addr)
                    continue
                
                # Exibe mensagem recebida e faz broadcast
                print(f"📩 Mensagem de {addr}: {data.decode()}")
                self.broadcast(data, addr)
                    
            except Exception as e:
                print(f"⚠️ Erro: {e}")
                break

if __name__ == '__main__':
    server = UDPServer()
    server.run()