
# Laporan Praktikum Minggu [3]
Topik: [Linux-fs-permission]

---

## Identitas
- **Nama**  : [Ani Ngismatul Hawa]  
- **NIM**   : [250202914]  
- **Kelas** : [1IKRB]

---

## Tujuan 
Mahasiswa bisa 

> Menggunakan perintah `ls, pwd, cd, cat` untuk navigasi file dan direktori.

> Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.

> Menjelaskan hasil output dari perintah Linux dasar.

> Menyusun laporan praktikum dengan struktur yang benar.

> Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
1. Sistem Operasi
Mengatur hubungan antara pengguna dan perangkat keras, serta mengelola proses, memori, dan file.

2. Kernel dan System Call
Kernel adalah inti sistem yang mengatur sumber daya.
System call digunakan program untuk meminta layanan dari kernel (misalnya membuka atau membaca file).

3. Manajemen File dan Izin Akses
Tiap file di Linux punya pemilik, grup, dan izin (`read, write, execute`).
Izin ini menjaga keamanan agar tidak semua orang bisa mengubah file.

4. Perintah Dasar
`chmod`: mengubah izin file.
`chown`: mengubah pemilik file.
`strace`: melihat system call yang dijalankan program.

---

## Langkah Praktikum
1. Setup Environment

Gunakan Linux (Ubuntu/WSL).
Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
`praktikum/week3-linux-fs-permission/`
Eksperimen 1 – Navigasi Sistem File Jalankan perintah berikut:

`pwd`
`ls -l`
`cd /tmp`
`ls -a`

Jelaskan hasil tiap perintah.

Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

2. Eksperimen 2 – Membaca File Jalankan perintah:

`cat /etc/passwd | head -n 5`

Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

3. Eksperimen 3 – Permission & Ownership Buat file baru:

`echo "Hello <NAME><NIM>" > percobaan.txt`

`ls -l percobaan.txt`

`chmod 600 percobaan.txt`

`ls -l percobaan.txt`

Analisis perbedaan sebelum dan sesudah chmod.

Ubah pemilik file (jika memiliki izin sudo):

`sudo chown root percobaan.txt`

`ls -l percobaan.txt`

Catat hasilnya.

4. Eksperimen 4 – Dokumentasi

Ambil screenshot hasil terminal dan simpan di:

`praktikum/week3-linux-fs-permission/screenshots/`

Tambahkan analisis hasil pada laporan.md.
Commit & Push

```git add .
git commit -m "Minggu 3 - Linux File System & Permission"
git push origin main
```

---

## Kode / Perintah
``` 
Hasil observasi perintah Linux dimasukkan ke dalam laporan.md
Screenshot hasil eksekusi disimpan di screenshots/.
Laporan lengkap tersimpan di laporan.md.
Semua hasil telah di-commit ke GitHub tepat waktu.

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Praktikum%20Linux%201.png)
![Screenshot hasil](./screenshots/Praktikum%20linux%202.png)

---

## Analisis
# 1. Hasil perintah 

|Perintah|Fungsi|Hasil yang ditunjukan|
|--------|------|---------------------| 
|Pwd| menunjukan direktori aktif| `/home/anihawa059/`|
|1s -1| menampilkan isi direktori secara detail| file `README-cloudshell.txt` |
|cd/tmp| pindah ke direktori sementara| berhasil masuk ke `/tmp`|
|1s -a| lihat semua file termasuk tersembunyi| daftar file sementara (cloud code, mini kube, VS code, dll)|

a. Direktori aktif

`pwd` hasilnya `/home/anihawa059`

`cd/tmp` hasilnya `/tmp` berpindah

b. Isi folder

`1s -a` `/tmp` termasuk file tersembunyi diawali `.` dan `..`

# 2. isi file dan struktur barisnya

|Kolom| Nama kolom| penjelasan| ex|
|-----|-----------|-----------|---|
|1| User| nama login pengguna| `root,demon.anihawa059` |
|2| UID | Nomor identitas unik untuk tiap user| `0` untuk `root`,`1000+` untuk user biasa|
|3| GID| Nomor identitas grup utama user mengacu ke `/etc/group`|`0,1000,dll`|
|4|Home| lokasi direktori pribadi user| `/root,/home/anihawa059`|
|5| shell| program yang dijalankan saat user login| `/bin/bash/usr/sbin/nologin`|
# 3. Analisis perbedaan sebelum dan sesudah chmod 
a. Sebelum Chmod 600

Izin `-rw-rw-r--` 
> 1. Pemilik bisa baca dan tulis
> 2. Grup bisa baca dan tulis
> 3. Orang lain bisa baca

b. Sesudah Chmod 600

 Izin `-rw-------`
> 1.  hanya pemilik bia baca dan tulis
> 2. Grup dan orang lain tidak bisa akses


---

## Kesimpulan
Dalam Linux, permission (izin akses) digunakan untuk mengatur siapa yang boleh membaca (read), menulis (write), atau menjalankan (execute) sebuah file atau folder.
Dari percobaan tadi terlihat bahwa:

> Hanya pemilik file (`root`) yang bisa mengakses file jika izinnya `rw-------.`

> Perintah `chmod` digunakan untuk mengubah izin akses.

> Perintah `chown` digunakan untuk mengubah pemilik file.ss


---

## Quiz
1. [Apa fungsi dari perintah `chmod?`]  
   **Jawaban:** 
   Fungsi perintah `chmod` (change mode) adalah untuk mengubah izin akses (permission) pada file atau direktori di sistem Linux. 
2. [pa arti dari kode permission `rwxr-xr--`?]  
   **Jawaban:**  
   `rwxr-xr-` artinya:
 Pemilik bisa baca, tulis, dan jalankan.
 Grup bisa baca dan jalankan.
 Orang lain hanya bisa baca saja.
3. [Jelaskan perbedaan antara `chown` dan `chmod`.]  
   **Jawaban:**  
```
chown → mengubah pemilik file atau folder (siapa yang punya).
Contoh: `chown root file.txt` → pemiliknya jadi root.

chmod → mengubah izin akses file atau folder (siapa yang boleh baca, tulis, jalankan).
Contoh: chmod 600 file.txt → hanya pemilik yang bisa baca dan tulis.
```
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
saat codingan menginput code ada code yang error 
- Bagaimana cara Anda mengatasinya? 
mengulangi dari awal dan menghapus yang salah 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
