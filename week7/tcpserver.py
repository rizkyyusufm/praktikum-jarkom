from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(5)
print('Server siap menerima koneksi client...')

while True :
    connectionSocket, addr = serverSocket.accept()
    print('Koneksi diterima dari: ', addr)

    sentence = connectionSocket.recv(2048).decode()
    print('Pesan diterima: ', sentence)

    modifiedSentence = sentence.upper()

    connectionSocket.send(modifiedSentence.encode())

    connectionSocket.close()