import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
broadcast_address = ('255.255.255.255', 6666)

while True:
    print("\n=== MENU BROADCAST (UDP) ===")
    print("1. Kirim Teks (Kata/Kalimat/Paragraf)")
    print("2. Kirim File (TXT/DOCX/PDF/JPG/PNG/MP3/MP4)")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        pesan = input("Masukkan teks: ")
        client.sendto(f"TEXT:{pesan}".encode('utf-8'), broadcast_address)
        print("[+] Broadcast teks terkirim.")
        
    elif pilihan == '2':
        path_file = input("Masukkan nama file (cth: foto.jpg): ")
        if os.path.exists(path_file):
            nama_file = os.path.basename(path_file)
            ukuran_file = os.path.getsize(path_file)
            
            # 1. Kirim info file dulu
            header = f"FILE:{nama_file}:{ukuran_file}"
            client.sendto(header.encode('utf-8'), broadcast_address)
            
            # 2. Kirim isi file binary-nya
            with open(path_file, "rb") as f:
                file_bytes = f.read()
                client.sendto(file_bytes, broadcast_address)
            print("[+] Broadcast file terkirim.")
        else:
            print("[-] File tidak ditemukan!")
            
    elif pilihan == '3':
        break
client.close()