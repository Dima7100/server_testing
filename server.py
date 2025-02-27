import socket

def start_server(host='0.0.0.0', port=65432):
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Привязываем сокет к адресу и порту
        server_socket.bind((host, port))
        # Слушаем входящие соединения
        server_socket.listen()
        print(f"Сервер запущен на {host}:{port}")

        while True:
            # Принимаем соединение
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Подключен клиент: {client_address}")
                # Получаем данные от клиента
                data = client_socket.recv(1024).decode('utf-8')
                print(f"Получено сообщение: {data}")
                # Отправляем ответ
                response = f"Сообщение принято, друг, вы написали: {data}"
                client_socket.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()