
# Laporan Praktikum Minggu [9]
Topik: Simulasi Algoritma Penjadwalan CPU


---

## Identitas
- **Nama**  : Ani Ngismatul Hawa
- **NIM**   : 250202914
- **Kelas** : 1IKRB

---

## Tujuan
> - Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
> - Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
> - Menyajikan output simulasi dalam bentuk tabel atau grafik.
> - Menjelaskan hasil simulasi secara tertulis.
> - Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
- Penjadwalan CPU adalah mekanisme dalam sistem operasi yang menentukan proses mana yang akan dieksekusi oleh CPU dan kapan proses tersebut dijalankan.
- Simulasi Algoritma Penjadwalan CPU adalah proses pemodelan dan pengujian berbagai algoritma penjadwalan dengan menggunakan data proses (seperti waktu kedatangan dan waktu eksekusi) untuk menganilisis kinerja algoritma tanpa harus menerapkannya langsung pada sistem nyata.

---

## Langkah Praktikum
1. Menyiapkan Dataset

Buat dataset proses minimal berisi:

|Proses|	Arrival Time|	Burst Time|
|------|------------|------------|
|P1	|0|	6|
|P2	|1|	8|
|P3	|2|	7|
|P4	|3|	3|
2. Implementasi Algoritma

Program harus:

- Menghitung waiting time dan turnaround time.
- Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
- Menampilkan hasil dalam tabel.
- Eksekusi & Validasi

- Jalankan program menggunakan dataset uji.
- Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
- Simpan hasil eksekusi (screenshot).
3. Analisis

- Jelaskan alur program.
- Bandingkan hasil simulasi dengan perhitungan manual.
- Jelaskan kelebihan dan keterbatasan simulasi.

5. Output yang Diharapkan
- Kode program simulasi di folder code/.
- Dataset uji di code/dataset.csv.
- Screenshot hasil eksekusi di screenshots/.
- Laporan lengkap di laporan.md.
- Semua hasil telah di-commit ke GitHub.

---

## Kode / Perintah

- Struktur folder

```praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```
- Push Github

> git add .

> git commit -m "Minggu 9 - Simulasi Scheduling CPU"

> git push origin main

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/Hasil%20Eksekusi.png)
---

## Analisis
Analisis Singkat Hasil Eksekusi FCFS

- Algoritma yang digunakan adalah FCFS (First Come First Serve) → proses dieksekusi sesuai urutan kedatangan: P1 → P2 → P3 → P4.

- P1 benar: datang paling awal, waiting time = 0, turnaround = 6.

- P2 dan P3: waiting time ditampilkan 0, seharusnya tidak 0 karena mereka menunggu proses sebelumnya selesai → ada kesalahan perhitungan waiting time.

- P4: waiting time dan turnaround sudah sesuai konsep FCFS.

Muncul SyntaxWarning invalid escape sequence '\t', karena penulisan string \t tidak aman.

---

## Kesimpulan
- Algoritma penjadwalan CPU berfungsi untuk mengatur urutan proses agar CPU bekerja lebih efisien. 
- Melalui simulasi, kita bisa melihat perbedaan waktu tunggu dan waktu penyelesaian setiap proses tergantung algoritma yang digunakan. 
- Setiap algoritma punya kelebihan dan kekurangan, sehingga pemilihan algoritma sangat memengaruhi kinerja sistem.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling? 

   **Jawaban:** 

Simulasi diperlukan supaya kita bisa menguji dan membandingkan algoritma schedulling dengan aman dan terkontrol, tanpa harus langsung menerpkannya di sistem nyata.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?

   **Jawaban:**  
- Perhitungan manual: Rentan salah hitung, memakan waktu lama, dan sulit dilacak kalau prosesnya banyak.
- Simulasi (program): Lebih cepat, akurat, dan kosisten meskipun datanya sangat besar. 

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

   **Jawaban:**  

Algoritma yang paling mudah diimplementasikan adalah FCFS (First Come First Serve). FCFS sederhana karena proses dijalankan sesuai urutan kedatangan. Tidsk perlu perhitungan rumit atau pengurutan berdasarkan burst time, cukup pakai antrian. Karena itu, FCFS paling mudah dipahami dan dibuat kodenya, terutama untuk pemula.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
menentukan code dalam pyhton agar tidak error saat dicoba
- Bagaimana cara Anda mengatasinya?  
membenarkan dan meneliti dengan jelas 
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
