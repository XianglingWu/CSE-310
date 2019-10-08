#import socket module
from socket import *
import sys # In order to terminate the program
import threading

def getConnection(connectionSocket,addr):
    try:
        dataRecv = connectionSocket.recv(1024)
        message = dataRecv.decode()#Fill in start #Fill in end
        print('Message received: '+message)
        if not message:
            return
        filename = message.split()[1]
        #print('File requested: '+filename)
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        f.close()
        httpHeader = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(httpHeader.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start 
        print("file not found")
        header = 'HTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(header.encode())
        response = '<html><body>\
        <h1>Error 404: File not found</h1>\
        </body></html>'
        connectionSocket.send(response.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 1997
serverSocket.bind(('',serverPort))
serverSocket.listen(2)
#print('server prepared.')
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    threading.Thread(target=getConnection,args=(connectionSocket,addr)).start()
serverSocket.close()
    #Terminate the program after sending the corresponding data 
sys.exit()