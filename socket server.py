import socket
import caesar
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 10082
sock.bind(('', PORT))
sock.listen(100)
print("Старт" + str(PORT))
conn, addr = sock.accept()
print("Підєднано: ", addr)

data = conn.recv(1024)
print(data.decode())
if input("Декодувати? Нажміть Y/n ") == "Y":
    print(caesar.decode(data.decode()))
else:
    pass
