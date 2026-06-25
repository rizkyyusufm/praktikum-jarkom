## **LAPORAN PRAKTIKUM MODUL 11**

## DHCP
DHCP adalah sebuah protokol atau aturan jaringan yang berfungsi untuk membagikan IP address (alamat IP) secara otomatis ke setiap perangkat (seperti HP, laptop, atau komputer) yang terhubung ke dalam suatu jaringan.

**Proses DHCP (DORA):**  
-**Discover** -> client mencari server DHCP  
-**Offer** -> server menawarkan IP  
-**Request** -> client meminta IP tersebut  
-**Acknowledge (ACK)** -> server mengonfirmasi pemberian IP  

**Jenis Pesan DHCP:**  
-**DHCP Discover**  
-**DHCP Offer**  
-**DHCP Request**  
-**DHCP ACK**  
-**DHCP NAK**  
-**DHCP Release**  

## 🔥 Tahap Implementasi DHCP

![image](../assets/image/week11/1.png)
<br>
<br>
Berdasarkan tangkapan layar di atas, proses diawali dengan paket **Discover**, di mana client mengirimkan pesan broadcast ke tujuan 255.255.255.255 dengan source 0.0.0.0 karena belum memiliki alamat IP. DHCP Server kemudian merespons dengan paket **Offer** untuk menawarkan alokasi IP address kepada client. Setelah menerima tawaran tersebut, client mengirimkan paket **Request** sebagai bentuk persetujuan atas IP yang ditawarkan. Proses penyerahan IP ini diselesaikan melalui paket **ACK (Acknowledgment)** yang dikirim oleh server sebagai konfirmasi akhir; setelah paket ACK ini diterima, client secara resmi mengonfigurasi dan menggunakan IP address tersebut pada sistemnya.

Selanjutnya, pada baris 36, terjadi proses DHCP Renewal (perpanjangan sewa). Client yang sudah memiliki IP address menghubungi DHCP Server kembali untuk memperpanjang masa sewa IP-nya, yang kemudian disetujui oleh server melalui paket **ACK** pada baris 37.

Aktivitas jaringan berlanjut pada baris 41, di mana client mengirimkan paket **Release** secara langsung ke arah server (192.168.1.1). Proses release ini bertujuan untuk melepaskan dan mengembalikan alokasi IP address yang sedang digunakan kembali ke dalam pool milik server, sehingga status IP pada client kembali kosong. Akibat dari pelepasan IP tersebut, pada baris 42 hingga 46, perangkat client mendeteksi ketiadaan alamat IP dan secara otomatis menginisiasi kembali siklus DORA dari awal.

## 📝 Kesimpulan

Berdasarkan hasil praktikum, dapat dipahami bahwa DHCP berfungsi untuk memberikan alamat IP secara otomatis kepada perangkat yang terhubung ke jaringan melalui proses DORA, yaitu Discover, Offer, Request, dan ACK. Dari hasil analisis Wireshark, terlihat bahwa client yang belum memiliki IP akan meminta konfigurasi ke DHCP Server, kemudian server memberikan penawaran IP hingga akhirnya IP berhasil dikonfigurasi pada client. Selain itu, praktikum juga menunjukkan adanya proses DHCP Renewal untuk memperpanjang masa sewa IP serta DHCP Release untuk melepaskan IP kembali ke server. Setelah IP dilepaskan, client akan kembali memulai proses DORA dari awal untuk memperoleh alamat IP baru.