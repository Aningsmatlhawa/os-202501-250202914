
# Laporan Praktikum Minggu [4]
Topik: [Proses user]

---

## Identitas
- **Nama**  : [Ani Ngismatul Hawa]  
- **NIM**   : [250202914]  
- **Kelas** : [1IKRB]

---

## Tujuan
>Menjelaskan konsep proses dan user dalam sistem operasi Linux.

>Menampilkan daftar proses yang sedang berjalan dan statusnya.

>Menggunakan perintah untuk membuat dan mengelola user.

>Menghentikan atau mengontrol proses tertentu menggunakan PID.

>Menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori


Teori dasar tentang proses dalam sistem operasi Linux. Proses adalah program yang sedang berjalan dan memiliki identitas unik yang disebut PID (Process ID). Saat perintah sleep 1000 & dijalankan, sistem membuat proses baru di latar belakang, dan dengan perintah ps aux atau grep, kita bisa melihat informasi detail seperti pengguna, status, dan penggunaan sumber daya. Proses dapat berada dalam berbagai status seperti running (berjalan), sleeping (menunggu), stopped, atau zombie. Sistem operasi juga mengatur prioritas proses melalui nilai PR dan NI agar penggunaan CPU tetap efisien. Selain itu, Linux mendukung konsep multiuser dan multitasking, yaitu memungkinkan banyak pengguna dan proses berjalan bersamaan tanpa saling mengganggu. Melalui praktikum ini, kita memahami bagaimana sistem operasi mengelola dan memantau proses yang aktif di dalamnya.

Semua program diatur seperti silsilah keluarga (hierarki proses) di mana setiap proses memiliki nomor identitas unik (PID), seperti terlihat dari perintah pstree. Kedua, untuk berinteraksi atau mengontrol program (misalnya, menghentikannya menggunakan perintah kill), pengguna harus mengikuti aturan bahasa yang ketat (sintaks shell). Kesalahan saat mencoba kill membuktikan bahwa sistem tidak akan bekerja jika perintahnya tidak lengkap, menegaskan bahwa kontrol proses bergantung pada identitas unik (PID) dan format perintah yang benar.

---

## Langkah Praktikum
1. Setup Environment

- Gunakan Linux (Ubuntu/WSL).
- Pastikan Anda sudah login sebagai user non-root.
- Siapkan folder kerja:
`praktikum/week4-proses-user/`
2. Eksperimen 1 –  Identitas User Jalankan perintah berikut:

`whoami
id
groups`

- Jelaskan setiap output dan fungsinya.
- Buat user baru (jika memiliki izin sudo):

`sudo adduser praktikan
sudo passwd praktikan` 
- Uji login ke user baru.
3. Eksperimen 2 – Monitoring Proses Jalankan:

`ps aux | head -10
top -n 1`

Jelaskan kolom penting seperti `PID, USER, %CPU, %MEM, COMMAND.`
- Simpan tangkapan layar `top `ke:
`praktikum/week4-proses-user/screenshots/top.png`
4. Eksperimen 3 – Kontrol Proses

- Jalankan program latar belakang:

`sleep 1000 &
ps aux | grep sleep`

- Catat PID proses sleep.
Hentikan proses:

`Kill <PID>`

- Pastikan proses telah berhenti dengan `ps aux | grep sleep.`

5. Eksperimen 4 – Analisis Hierarki Proses Jalankan:

`pstree -p | head -20`

- Amati hierarki proses dan identifikasi proses induk `(init/systemd).`
- Catat hasilnya dalam laporan.
Commit & Push

`git add .
git commit -m "Minggu 4 - Manajemen Proses & User"
git push origin main`


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
- Hasil observasi seluruh perintah dimasukkan ke dalam `laporan.md.`

- Screenshot hasil eksekusi disimpan di folder `screenshots/.`

- laporan lengkap tersimpan di `laporan.md.`
- Semua hasil telah di-commit ke GitHub tepat waktu.
# Eksperimen 1
`whoami
id
groups`

`sudo adduser praktikan
sudo passwd praktikan`

# Eksperimen 2
`ps aux | head -10
top -n 1`

# Eksperimen 3
`Sleep 1000 &
ps aux | grep sleep`
`kill <PID>`

# Eksperimen 4
`pstree -p | head -20`

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/Eksperimen%201.png)
![Screenshot hasil](./screenshots/sudo.png)
![Screenshot hasil](./screenshots/Esperimen%202.png)
![Screenshot hasil](./screenshots/sleep.png)
![Screenshot hasil](./screenshots/sleep%202.png)
![Screenshot hasil](./screenshots/Eksperimen%203.png)
![Screenshot hasil](./screenshots/kill.png)
![Screenshot hasil](./screenshots/Eksperimen%204.png)

# 1. Eksperimen 1 

|Perintah|Fungsi|Output|
|--------|------|-----|
|`whoami`|Menampilkan nama pengguna (username) yang sedang aktif di shell saat ini|`matulsyantik`|
|`id`|Menampilkan informasi identitas pengguna, termasuk:`UID (User ID)`, `GID (Group ID)`, `Groups` (kelompok yang diikuti user)| `uid=1000(matulsyantik) gid=1000(matulsyantik) groups=1000(matulsyantik),4(adm),27(sudo),996(docker)`|
|`groups`|Menampilkan daftar grup yang diikuti oleh pengguna saat ini.|`matulsyantik adm sudo docker`| 

# 2. Eksperimen 2

|Kolom|Keterangan|
|-----|----------|
|PID|menunjukkan nomor unik proses|
|USER|menunjukkan siapa yang menjalankan prosesnya|
|%CPU|Menunjukkan seberapa besar penggunaan prosesor oleh proses tersebut. Nilainya dalam persen (%). Semakin tinggi nilainya, semakin besar beban CPU dari proses itu.|
|%MEM|Menunjukkan berapa persen memori RAM yang digunakan oleh proses tersebut. Ini membantu mengetahui proses mana yang paling banyak memakai memori.|
|COMMAND|menampilkan nama program yang dijalankan.|

# 3. Eksperimen 3

`sleep 1000 &` Perintah ini menjalankan program sleep selama 1000 detik di background (ditandai dengan tanda &).
Sistem kemudian menampilkan [1] 1397, yang berarti ini adalah job number 1 dengan PID (Process ID) 1397. PID ini adalah identitas unik dari proses sleep yang baru saja dibuat.

`ps aux | grep sleep` Perintah ini menampilkan semua proses yang sedang berjalan (ps aux) dan memfilter hasilnya hanya yang berisi kata “sleep” menggunakan grep.

`kill <PID>`
Perintah kill digunakan untuk mengirimkan sinyal kepada sebuah proses, biasanya untuk mengakhirinya. <PID> adalah Placeholder yang seharusnya diganti dengan Process ID (ID Proses) yang valid dari proses yang ingin dihentikan.

`pstree -p | head -20`
Dalam sistem Linux, semua proses, pada akhirnya, adalah turunan dari satu proses induk utama yang dikenal sebagai proses init atau systemd (PID 1).
Dalam lingkungan Linux tradisional, proses dengan PID 1 secara historis adalah proses init (seperti SysVinit, upstart, atau yang paling umum saat ini, systemd). Proses inilah yang pertama kali dijalankan oleh kernel dan merupakan "induk" dari semua proses lain di sistem.

# Diagram Pohon

```
bash(1)

├─ dockerd(247)
│  ├─ containerd(286)
│  │  ├─ {containerd}(299)
│  │  ├─ {containerd}(300)
│  │  ├─ {containerd}(301)
│  │  ├─ {containerd}(303)
│  │  ├─ {containerd}(304)
│  │  └─ {containerd}(307)
│  ├─ {dockerd}(245)
│  ├─ {dockerd}(255)
│  ├─ {dockerd}(256)
│  ├─ {dockerd}(257)
│  ├─ {dockerd}(265)
│  ├─ {dockerd}(270)
│  ├─ {dockerd}(309)
│  ├─ {dockerd}(308)
│  └─ {dockerd}(25906)
│
├─ logger(26)
│
└─ python(25)
   ├─ editor-proxy(289)
   │  └─ runuser(517)
   │     └─ sh(518)
   │        └─ node(535)
   │           ├─ node(1259)
   │           │  └─ cloudcode_cli(1325)
   │           │     ├─ {cloudcode_cli}(…)
   │           │     ├─ {cloudcode_cli}(…)
   │           │     └─ {cloudcode_cli}(…)

```

---

## Analisis
- Jelaskan hubungan antara user management dan keamanan sistem Linux.

> User management dan keamanan sistem Linux saling berhubungan karena pengaturan pengguna membantu melindungi sistem. Setiap pengguna punya akun dan izin sendiri untuk mengakses file atau menjalankan perintah. Dengan begitu, hanya pengguna tertentu (seperti root) yang bisa mengubah bagian penting sistem. Pembagian pengguna dan grup juga membuat izin lebih mudah diatur dan aktivitas bisa diawasi. Jadi, pengelolaan pengguna yang baik membantu mencegah akses ilegal dan menjaga sistem tetap aman.

Dari praktikum ini, bisa disimpulkan bahwa sistem operasi Linux memiliki cara yang teratur dalam mengelola proses dan pengguna. Saat perintah sleep 1000 & dijalankan, sistem membuat proses baru di latar belakang dengan PID tertentu, yang menunjukkan bagaimana Linux memberi identitas unik untuk setiap proses. Melalui perintah seperti ps aux dan grep, kita dapat memantau proses, melihat siapa penggunanya, serta mengetahui statusnya. Hal ini menunjukkan bahwa Linux tidak hanya mengatur jalannya proses, tetapi juga menjaga keamanan dengan membatasi hak akses tiap pengguna. Jadi, praktikum ini memperlihatkan hubungan antara manajemen proses dan manajemen pengguna dalam menjaga sistem tetap teratur dan aman.

Praktikum ini juga menganalisis dua interaksi penting di Linux: melihat struktur program dan mencoba mengontrolnya. Analisis pohon proses (pstree) berhasil menunjukkan bahwa sistem menjalankan layanan kontainer (dockerd) dan alat pengembangan (cloudcode_cli) dalam hierarki yang terstruktur berdasarkan ID unik (PID). Sementara itu, percobaan kontrol (kill) gagal karena pengguna melanggar aturan bahasa terminal (sintaks), yang menunjukkan bahwa kontrol sistem bergantung pada penargetan PID yang tepat dan penggunaan perintah yang benar. Intinya, praktikum ini adalah tentang identifikasi proses sebagai langkah pertama menuju kontrol sistem yang berhasil.

---

## Kesimpulan
 Linux bisa mengatur proses dan pengguna dengan baik agar sistem tetap aman dan stabil. Setiap proses punya nomor unik (PID) dan bisa dicek dengan perintah seperti ps aux. Pengaturan hak akses juga memastikan hanya pengguna tertentu yang bisa mengubah bagian penting sistem.
 Praktikum ini menegaskan bahwa untuk mengelola sistem Linux, kita harus terlebih dahulu memahami hierarki program yang berjalan (pstree) untuk mendapatkan ID unik (PID) mereka. Upaya untuk menghentikan program (kill) yang gagal menunjukkan bahwa kontrol hanya bisa dilakukan jika kita menggunakan PID yang benar dan mengikuti aturan bahasa terminal (sintaks) secara persis. Singkatnya, identifikasi yang benar adalah kunci untuk kontrol sistem yang berhasil.

---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?  
   **Jawaban:**  

   Proses **init** atau **systemd** berfungsi sebagai proses pertama yang berjalan saat Linux dinyalakan. Ia mengatur dan menjalankan semua layanan penting sistem, memantau proses lain, serta memastikan sistem berjalan dengan benar dari awal hingga dimatikan.

2. Apa perbedaan antara kill dan killall? 
   **Jawaban:**  

   Perintah **`kill`** menghentikan proses berdasarkan **nomor PID**, sedangkan **`killall`** menghentikan **semua proses dengan nama yang sama**.

3. Mengapa user root memiliki hak istimewa di sistem Linux?
   **Jawaban:** 

    User **root** punya hak istimewa karena dia adalah **admin utama** di Linux. Root bisa mengubah apa pun di sistem, termasuk file dan pengaturan, supaya bisa mengelola dan memperbaiki sistem sepenuhnya.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
Saat menggunakan Linux atau Cloudshell, sempat beberapa error karena sudah pernah digunakan sebelumnya 
- Bagaimana cara Anda mengatasinya?  
Menggunakan akun lain agar bisa terdeteksi

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
