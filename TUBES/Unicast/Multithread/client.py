import socket
import os

def send_file(client_socket, filename): 
    # Logika dasar kirim file
    if os.path.exists(filename):
        filesize = os.path.getsize(filename)
        client_socket.send(f"FILE:{filename}:{filesize}".encode())
        with open(filename, "rb") as f:
            while (chunk := f.read(1024)):
                client_socket.send(chunk)
        print("File terkirim!")
    else:
        print("File tidak ditemukan.")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.132.236.125', 5555)) 

while True:
    print("\n--- MENU UNICAST ---")
    print("1. Kirim Teks (Kata/Kalimat/Paragraf)")
    print("2. Kirim File (Doc/Img/Audio/Video)")
    print("3. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == '1':
        pesan = input("Masukkan pesan: ")
        client.send(f"TEXT:{pesan}".encode())
    elif pilihan == '2':
        nama_file = input("Masukkan nama file (contoh: tugas.pdf): ")
        send_file(client, nama_file)
    elif pilihan == '3':
        break