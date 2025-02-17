#UPD SOCKETS
import socket 
#database adaptor
import psycopg2
from psycopg2 import sql

#send to 7500
#recieve from 7501


with open("network.txt", "r") as file:
        localIp = file.read()
localPort = 7501
bufferSize = 1024

#define database connection parameters
config = {
    'dbname': 'photon'
}

#msgFromServer = "Hello world, Hello server\n"
#bytesToSend = str.encode(msgFromServer)

#creating server socket that will listen for data
UPDServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#binds server to the specific ip/port combination
UPDServerSocket.bind((localIp, localPort))

print("UPD Server up and listening")

#try to connect to database
try:
    conn = psycopg2.connect(**config)
    cur = conn.cursor()

    #execute a query
    cur.execute("SELECT version();")

    #fetch and display the result
    version = cur.fetchone()
    print(f"Connected to - {version}")

except Exception as error:
    print(f"Error connecting to SQL database: {error}")
    
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

        #separate client message into player and id
        split_msg = (message.decode()).split(":")

        #try to add player & id to database
        try:
            cur.execute('''
                INSERT INTO players (id, codename)
                VALUES (%s, %s);
            ''', (split_msg[0], split_msg[1]))

            #commit the changes
            conn.commit()

            #fetch and display the data from the table
            cur.execute("SELECT * FROM players;")
            rows = cur.fetchall()
            for row in rows:
                print(row)

        except Exception as error:
            print(f"Error adding clientMsg to database: {error}")
        
        msgFromServer = "I will be adding:{}\n".format(message.decode())
        bytesToSend = str.encode(msgFromServer)

        #sends a message back to the client through its original address
        UPDServerSocket.sendto(bytesToSend, address)

except KeyboardInterrupt:
    #closing socket
    UPDServerSocket.close()

finally:
    #close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()

"""""
idea for socket selection, uses gui and dropdown. NEED: how interfaces with UDP work
import socket
import fcntl
import struct
import os
from tkinter import *

# Get the list of network interfaces
def get_network_interfaces():
    interfaces = []
    for interface in os.listdir('/sys/class/net/'):
        if os.path.exists(f'/sys/class/net/{interface}/address'):
            interfaces.append(interface)
    return interfaces

# Function to select a network interface and send data via UDP
def select_network():
    selected_interface = variable.get()  # Get the selected network interface
    print("Selected Network Interface:", selected_interface)
    
    # Create the UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Get the IP address of the selected interface
    ip_address = get_ip_address(selected_interface)
    print("IP Address of selected interface:", ip_address)
    
    # Set the socket to use the selected IP address
    udp_socket.bind((ip_address, 12345))  # Example port
    
    # Send a test message (you can customize this part)
    udp_socket.sendto(b"Hello UDP", ("<destination_ip>", 12345))
    udp_socket.close()

# Function to get the IP address of the selected interface
def get_ip_address(interface):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', interface[:15].encode('utf-8'))
    )
    return socket.inet_ntoa(ip_address[20:24])

# Tkinter GUI Setup
master = Tk()

# Get the available network interfaces
interfaces = get_network_interfaces()
variable = StringVar(master)
variable.set(interfaces[0])  # Default to the first interface

# Create a dropdown menu for network interface selection
w = OptionMenu(master, variable, *interfaces)
w.pack()

# Button to trigger network selection
button = Button(master, text="Select Network", command=select_network)
button.pack()

master.mainloop()

"""

