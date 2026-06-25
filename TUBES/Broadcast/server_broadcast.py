import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 6666))

print("=== SERVER BROADCAST READY ===")
print("Mendengarkan data broadcast di port 6666...\n")

while True:
    try:
        data, addr = server.recvfrom(65535)
        if not data:
            continue
            
        # Cek apakah yang masuk Teks atau File
        header = data.decode('utf-8', errors='ignore')
        
        if header.startswith("TEXT:"):
            print(f"[BROADCAST TEKS] Dari {addr}: {header[5:]}")
            
        elif header.startswith("FILE:"):
            # Format: FILE:nama_file:ukuran_file
            _, nama_file, ukuran_file = header.split(":")
            ukuran_file = int(ukuran_file)
            print(f"[BROADCAST FILE] Menerima {nama_file} ({ukuran_file} bytes) dari {addr}...")
            
            # Terima isi file binary-nya (paket berikutnya)
            file_data, _ = server.recvfrom(65535)
            
            nama_file_baru = f"broadcast_received_{nama_file}"
            with open(nama_file_baru, "wb") as f:
                f.write(file_data)
                
            print(f"[SUKSES] File disimpan: '{nama_file_baru}'\n")
            
    except Exception as e:
        print(f"Error: {e}")