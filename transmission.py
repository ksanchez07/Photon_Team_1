import socket


class Transmission():
    def __init__(self):
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    #transmit_string doesnt work *sad emoji*
    def transmit_string(self, message, port):
        with open("network.txt", "r") as file:
            localIp = file.read()
    
        clientAddressPort = (localIp, port)
        
        
        self.UDPClientSocket.sendto(str.encode(str(message)), clientAddressPort)

    def transmit(self, message, port):
       with open("network.txt", "r") as file:
           localIp = file.read()
       clientAddressPort = (localIp, port)
       
        
       self.UDPClientSocket.sendto(str.encode(str(message)), clientAddressPort)



       