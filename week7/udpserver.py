from socket import *

#Membuat socket untuk server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Menghubungkan (bind)
serverSocket.bind(
    ('', serverPort)
)

print("[SERVER] server siap digunakan")

running = True
while running :
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode()

    if decodedMessage.lower() == "exit" :
        print("[SYSTEM] server telah diberhentikan ")
        running = False 
        continue

    modifiedMessage = decodedMessage.upper()
    print("[Server] diterima dari ", clientAddress, "message : ", decodedMessage)

    #Mengirim ke klien
    serverSocket.sendto(
        modifiedMessage.encode(),
        clientAddress
    )

serverSocket.close()
print("[SYSTEM] Koneksi telah ditutup")