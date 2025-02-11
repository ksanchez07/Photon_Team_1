import socket

#inputting player information
msgFromClient = input("Player:Equipment ID\n")
bytesToSend = str.encode(msgFromClient)

#the server we are sending the information to
serverAddressPort = ("127.0.0.1", 7501)
bufferSize = 1024

#creating client side socket
UPDClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#sending the information to ther server
UPDClientSocket.sendto(bytesToSend, serverAddressPort)

#recieving message from server, decoding, and printing
msgFromServer = UPDClientSocket.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0].decode())
print(msg)
