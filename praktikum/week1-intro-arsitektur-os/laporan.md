
# Laporan Praktikum Minggu [1]
Topik: [Analisis arsitektur kernel dan model sistem operasi]

---

## Identitas
- **Nama**  : [Ani Ngismatul Hawa]  
- **NIM**   : [250202914]  
- **Kelas** : [1IKRB ]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu memahami cara kerja kernel dan sisem operasi, meningkatkan modularitas.
> Membandingkan model arsitektur OS
> Mengidentifikasi komponen utama OS
> Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu

---

## Dasar Teori
 Monolithic kernel : semua layanan inti sistem operasi dijalankan dalam kernel space  yang sama
 Micro kernel      : yang dijalankan hanya fungsi-fungsi paling esensial di ruang kernel,seperti manajemen proses dan komuinikasi antar proses.
 Layered           : disusun dalam lapisan-lapisan terpisah yang memiliki fungsi berbeda, seperti lapisan presentasi, dsb.

---

## Langkah Praktikum
1. Membaca dan memahami materi bagaimana cara bekerja OS atau Sistem operasi dengan rinci dan jelas.  
2. Perintah yang dijalankan.
 ```bash
uname -a
whoami
lsmod | head
dmesg | head
```

3. Membuat diagram arsitektur menggunakan ala bantu (Draw.io).  
5. Commit message yang digunakan
 Hasil Laporan
```praktikum/week1-intro-arsitektur-os/laporan.md```
Hasil Diagram
```praktikum/week1-intro-arsitektur-os/screenshoots/diagram-os.png```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```git add.
git commit-m "Minggu 1"
git push origin main
```

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![schreenshots/.](screenshots/example.png)

---

## Analisis
- makna hasil percobaan antara lain menganalisis kelebihan dan kekurangan setiap os, mengidentifikasi suatu masalah pada os  .  
- arsitektur os adalah struktur dasar,kernel adalah inti yang menghubungkan software dan hardware, sistem call adalah suatu mekanisme yang dapat digunakan aplikasi untuk meminta layanan dari kernel, dan sementara itu aplikasi tidak dapat langsung mengakses hardware ataupun sebaliknya .  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)? linux lebih efisiens tetapi windows mempermudah hardware melalui sistem komersialnya  

---

## kesimpulan yang saya ambil adalah
perbedaan sistem operasi seperti kernel, sistem call dan arsitektur os sangat berbeda satu sama lain,selain itu saya  jadi tahu bagaimana cara bekerja sistem operasi, dan mengetahui sisi linux aaupun windows, saya lebih mudah mengidentifikasi software bagaimana dan juga hardware .

---

## Quiz
1. [jelaskan fungsi utama sistem operasi]  
   **Jawaban: memanajemen proses,menjadi perantara antara software dan hardware,menjalankan dan mengatur aplikasi.**  
2. [jelaskan perbedaan antara kernel mode dan user mode]  
   **Jawaban: user mode bisa menyentuh os tetapi hanya bisa menjalankan aplikasi yang terlihat dengan terbatas sedangkan kernel mode mempunyai hak penuh atas os yang tak terlihat oleh user maupun yang terlihat oleh user,dan mempunyai hak istimewa terhadap hardware**  
3. [sebutkan contoh OS dengan arsitektur monolithic dan microcernel]  
   **Jawaban:monolithic antara lain, Linux, dan Windows, sedangkan Mikrokernel, QNX, dan minix**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? cara pengerjaan dengan membuat code,kesalahan update didashboard github,membaca referensi dari beberapa sumber 
- Bagaimana cara Anda mengatasinya? melihat tutorial diaplikasi yt, mengulang kembali tugas (revisi), memilih 1 buku yang mengacu pada materi kali ini.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
