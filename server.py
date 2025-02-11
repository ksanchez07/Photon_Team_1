#UPD SOCKETS
import socket


localIp = "127.0.0.1"
localPort = 7501
bufferSize = 1024

#msgFromServer = "Hello world, Hello server\n"
#bytesToSend = str.encode(msgFromServer)

#creating server socket that will listen for data
UPDServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#binds server to the specific ip/port combination
UPDServerSocket.bind((localIp, localPort))

print("UPD Server up and listening")

#while program is running
try:
    while (True):

        #stores message from client and ip address(up to 1024 bytes)
        bytesAddressPair = UPDServerSocket.recvfrom(bufferSize)
        message, address = bytesAddressPair
    

        #formatting message from client into readable strings
        #.decode() removes unwanted stuff/symbols from the message
        clientMsg = "Message from client:{}\n".format(message.decode())
        clientIp = "Client IP Address: {}".format(address)

        print(clientMsg, end= "")
        print(clientIp)
        print("")

        msgFromServer = "I will be adding:{}\n".format(message.decode())
        bytesToSend = str.encode(msgFromServer)

        #sends a message back to the client through its original address
        UPDServerSocket.sendto(bytesToSend, address)

except KeyboardInterrupt:
    #closing socket 
    UPDServerSocket.close()
