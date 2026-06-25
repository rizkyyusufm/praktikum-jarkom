import socket
import struct

multicast_group = '224.1.1.1' # ip grup multicast
server_address = ('', 7777) # string ksong berarti server siap menerima data dari jaringan manapun

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # agar bisa bind ke alamat yang sama jika server direstart
server.bind(server_address) # bind ke port untuk menerima data multicast

ip_laptop_server = '10.132.236.59'

# group = socket.inet_aton(multicast_group) # mengubah string IP menjadi format biner 4 byte
# mreq = struct.pack('4s4s', group, socket.inet_aton(ip_laptop_server)) # mengisi ruang L dengan perintah untuk menerima data
# server.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq) # mengatur konfigurasi pada level protokol

print(f"=== SERVER MULTICAST READY (Grup: {multicast_group}) ===")

while True:
    try:
        data, addr = server.recvfrom(65535)
        if not data:
            continue
            
        header = data.decode('utf-8', errors='ignore')
        
        if header.startswith("TEXT:"):
            print(f"[MULTICAST TEKS] Dari {addr}: {header[5:]}")
            
        elif header.startswith("FILE:"):
            _, nama_file, ukuran_file = header.split(":")
            ukuran_file = int(ukuran_file)
            print(f"[MULTICAST FILE] Menerima {nama_file} ({ukuran_file} bytes) dari {addr}...")
            
            file_data, _ = server.recvfrom(65535)
            
            nama_file_baru = f"multicast_received_{nama_file}"
            with open(nama_file_baru, "wb") as f:
                f.write(file_data)
                
            print(f"[SUKSES] File disimpan: '{nama_file_baru}'\n")
            
    except Exception as e:
        print(f"Error: {e}")