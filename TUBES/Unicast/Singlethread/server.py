import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Agar bisa bind ke alamat yang sama jika server direstart
server.bind(('', 5555)) # Bind ke localhost dan port
server.listen(1) 

print("Server standby di port 8081...")
conn, addr = server.accept()

while True:
    try:
        data = conn.recv(1024).decode() 
        if not data: break 
        
        # Cek tipe data yang masuk
        if data.startswith("TEXT:"):
            print(f"Pesan Teks: {data[5:]}")
        
        elif data.startswith("FILE:"):
            # Format: FILE:nama:ukuran
            _, fname, fsize = data.split(":")
            fsize = int(fsize)
            print(f"Menerima file: {fname} ({fsize} bytes)")
            
            with open(f"received_{fname}", "wb") as f:
                bytes_received = 0
                while bytes_received < fsize:
                    chunk = conn.recv(1024)
                    f.write(chunk)
                    bytes_received += len(chunk)
            print("File berhasil disimpan.")
            
    except Exception as e:
        print(f"Error: {e}")
        break

conn.close()