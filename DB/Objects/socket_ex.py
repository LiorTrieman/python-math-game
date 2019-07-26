'''import socket

my_socket = socket.socket()
# Connect to server port 2880
my_socket.connect(('127.0.0.1', 1729))
# send message to server
my_socket.send("Hi Lior")
# receive info from server
data = my_socket.recv(1024)
print("The server sent" + data)

my_socket.close()

'''
from PIL import ImageGrab
im = ImageGrab.grab()
im.save('C:\screen.jpg')
