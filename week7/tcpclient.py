from socket import *

serverName = 'localhost'
serverPort = 12000

# Create client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server
clientSocket.connect((serverName, serverPort))

# Send message to server
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(2048)
print('From Server: ', modifiedSentence.decode())

clientSocket.close()