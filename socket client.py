import socket
import caesar


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 10082))
    _text = input()
    if _text[0] == "/":
        data = caesar.caesar(_text)
        s.sendall(str(data[1:len(data)]).encode())
    else:
        data = s.sendall(_text.encode())
