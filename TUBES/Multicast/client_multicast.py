import socket
import struct
import os

ip_target_server = '10.132.236.125'
multicast_group = (ip_target_server, 7777)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 1)
client.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

while True:
    print("\n=== MENU MULTICAST (UDP GROUP) ===")
    print("1. Kirim Teks (Kata/Kalimat/Paragraf)")
    print("2. Kirim File (TXT/DOCX/PDF/JPG/PNG/MP3/MP4)")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        pesan = input("Masukkan teks untuk grup: ")
        client.sendto(f"TEXT:{pesan}".encode('utf-8'), multicast_group)
        print("[+] Multicast teks terkirim.")
        
    elif pilihan == '2':
        path_file = input("Masukkan nama file (cth: tugas.pdf): ")
        if os.path.exists(path_file):
            nama_file = os.path.basename(path_file)
            ukuran_file = os.path.getsize(path_file)
            
            # 1. Kirim info file
            header = f"FILE:{nama_file}:{ukuran_file}"
            client.sendto(header.encode('utf-8'), multicast_group) 
            
            # 2. Kirim bytes file
            with open(path_file, "rb") as f: 
                file_bytes = f.read() 
                client.sendto(file_bytes, multicast_group) 
            print("[+] Multicast file terkirim.")
        else:
            print("[-] File tidak ditemukan!")
            
    elif pilihan == '3':
        break
client.close()