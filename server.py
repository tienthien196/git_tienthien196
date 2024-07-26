import socket
import threading

# Danh sách các client đang kết nối
clients = []
nicknames = []

# Khởi tạo server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen()

# Broadcast message tới tất cả các client
def broadcast(message):
    for client in clients:
        client.send(message)

# Xử lý kết nối của mỗi client
def handle(client):
    while True:
        try:
            # Nhận message từ client và broadcast
            message = client.recv(1024)
            broadcast(message)
        except:
            # Ngắt kết nối và loại bỏ client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} đã rời khỏi phòng chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Nhận kết nối từ client mới
def receive():
    while True:
        client, address = server.accept()
        print(f"Kết nối từ {str(address)}")

        # Yêu cầu nickname từ client
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname của client là {nickname}')
        broadcast(f'{nickname} đã tham gia phòng chat!'.encode('utf-8'))
        client.send('Kết nối tới server thành công!'.encode('utf-8'))

        # Bắt đầu thread để xử lý kết nối của client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('Server đang lắng nghe...')
receive()
