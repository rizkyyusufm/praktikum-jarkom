import socket
import threading # Untuk menangani banyak client secara bersamaan

def handle_client(conn, addr): # Fungsi untuk menangani komunikasi dengan setiap client
    print(f"[NEW CONNECTION] {addr} terhubung.") 
    while True:
        try:
            # Terima indikator jenis data
            header = conn.recv(1024).decode('utf-8') 
            if not header:
                break
            
            # Logika Teks
            if header.startswith("TEXT:"):
                print(f"[{addr} - TEKS]: {header[5:]}")
                
            # Logika File
            elif header.startswith("FILE:"):
                _, nama_file, ukuran_file = header.split(":")
                ukuran_file = int(ukuran_file)
                print(f"[{addr} - FILE]: Menerima {nama_file} ({ukuran_file} bytes)")
                
                conn.send("READY".encode('utf-8'))
                
                with open(f"received_{nama_file}", "wb") as f:
                    bytes_terunduh = 0
                    while bytes_terunduh < ukuran_file:
                        chunk = conn.recv(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                        bytes_terunduh += len(chunk)
                print(f"[SUKSES] File dari {addr} disimpan dengan nama 'received_{nama_file}'")
                
        except ConnectionResetError: 
            break
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan pada {addr}: {e}") 
            break

    print(f"[DISCONNECTED] {addr} terputus.")
    conn.close()

# Setup Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Agar bisa bind ke alamat yang sama jika server direstart
server.bind(('', 5555)) # Bind ke localhost dan port yang sama dengan client
server.listen() 

print("=== SERVER UNICAST MULTITHREAD RUNNING ===")
print("Menunggu banyak koneksi sekaligus...\n")

# PASTIKAN BAGIAN INI MENGGUNAKAN WHILE TRUE:
while True:
    try:
        conn, addr = server.accept()
        # Membuat thread baru untuk setiap client yang masuk
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        # Mencetak jumlah client yang aktif (dikurang 1 karena thread utama server tidak dihitung)
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("\nServer dimatikan oleh pengguna.")
        break

server.close()