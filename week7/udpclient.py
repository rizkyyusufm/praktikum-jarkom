from socket import *

serverName = "localhost"
serverPort = 12000

#AF_INET = ip addr v4| SOCK_DGRAM = UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

running = True

while running :
    message = input("> ")
    if message.lower() == "exit" :
        clientSocket.sendto(
            message.encode(),
            (serverName, serverPort)
        )
        print("[SYSTEM} Keluar dari program")
        running = False
        continue

    #Mengirim pesan
    clientSocket.sendto(
        #Contoh : Jarkom -> 101110111
        message.encode(),
        (serverName, serverPort)
    )

    #Menerima pesan
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("[SYSTEM] Pesan telah diterima dari: ", serverAddress)
    print(modifiedMessage.decode())

clientSocket.close()