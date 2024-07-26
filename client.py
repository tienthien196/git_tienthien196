import socket
import threading

# Kết nối tới server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Nhận tin nhắn từ server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Ngắt kết nối nếu có lỗi
            print("Có lỗi xảy ra!")
            client.close()
            break

# Gửi tin nhắn tới server
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Nhập nickname của client
nickname = input("Nhập nickname: ")

# Bắt đầu các thread nhận và gửi tin nhắn
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()