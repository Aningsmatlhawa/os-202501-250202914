
# Laporan Praktikum Minggu [10]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)
---

## Identitas
- **Nama**  : Ani Ngismatul Hawa
- **NIM**   : 250202914  
- **Kelas** : 1IKRB

---

## Tujuan
- Mengimplementasikan algoritma page replacement FIFO dalam program.
- Mengimplementasikan algoritma page replacement LRU dalam program.
- Menjalankan simulasi page replacement dengan dataset tertentu.
- Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
- Menyajikan hasil simulasi dalam laporan yang sistematis.
---

## Dasar Teori
- Manajemen Memori adalah pengelolaan RAM oleh sistem operasi agar proses berjalan efisien.
Page Replacement digunakan saat memori penuh untuk menentukan halaman (page) mana yang harus diganti.

- FIFO (First In First Out) mengganti page yang paling awal masuk ke memori. Algoritma ini sederhana tetapi kurang efisien karena tidak memperhatikan penggunaan page.

- LRU (Least Recently Used) mengganti page yang paling lama tidak digunakan. Algoritma ini lebih efisien dan menghasilkan page fault lebih sedikit, namun implementasinya lebih kompleks.

- Kesimpulan: FIFO mudah diterapkan, sedangkan LRU lebih optimal dalam kinerja memori.

---

## Langkah Praktikum
1. Menyiapkan Dataset

Gunakan reference string berikut sebagai contoh:

> 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
Jumlah frame memori: 3 frame.

2. Implementasi FIFO

Simulasikan penggantian halaman menggunakan algoritma FIFO.
Catat setiap page hit dan page fault.
Hitung total page fault.

3. Implementasi LRU

Simulasikan penggantian halaman menggunakan algoritma LRU.
Catat setiap page hit dan page fault.
Hitung total page fault.

4. Eksekusi & Validasi

Jalankan program untuk FIFO dan LRU.
Pastikan hasil simulasi logis dan konsisten.
Simpan screenshot hasil eksekusi.

5. Analisis Perbandingan

Buat tabel perbandingan seperti berikut:

|Algoritma	|Jumlah Page Fault	|Keterangan|
|---|---|---|
|FIFO	|...|	...|
|LRU	|...	|...|

Jelaskan mengapa jumlah page fault bisa berbeda.
Analisis algoritma mana yang lebih efisien dan alasannya.

6. Commit & Push

```git add .```
```git commit -m "Minggu 10 - Page Replacement ```
```FIFO & LRU"```
```git push origin main```

- Output yang Diharapkan
- Kode program simulasi di folder code/.
- Dataset uji di code/reference_string.txt.
- Screenshot hasil simulasi di screenshots/.
- Laporan lengkap di laporan.md.
- Semua hasil telah di-commit ke GitHub.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:

2. Struktur folder (sesuaikan dengan template repo):
```
- praktikum/week10-page-replacement/
├─ code/
│  ├─ page_replacement.*
│  └─ reference_string.txt
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
```
2. Menyiapkan Dataset

Gunakan reference string berikut sebagai contoh:

```7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2```

3. Buat tabel perbandingan seperti berikut:

|Algoritma|	Jumlah Page Fault	|Keterangan|
|-----|-----|-----|
|FIFO|	...|	...|
|LRU|	...|	...|
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

- **FIFO**
![Screenshot hasil](./screenshots/FIFO.png)
- **LRU**
![Screenshot hasil](./screenshots/LRU.png)
- **Hasil**
![Screenshot hasil](./screenshots/Perbandingan.png)

---

## Analisis
1. **Tabel FIFO**

| Langkah | Page | Frame 1 | Frame 2 | Frame 3 | Status     |
| --------| ---- | ------- | ------- | ------- | ---------- |
|    1    |   7  |    7    |    -    |    -    | Page Fault |
|    2    |   0  |    7    |    0    |    -    | Page Fault |
|    3    |   1  |    7    |    0    |    1    | Page Fault |
|    4    |   2  |    2    |    0    |    1    | Page Fault |
|    5    |   0  |    2    |    0    |    1    | Page Hit   |
|    6    |   3  |    2    |    3    |    1    | Page Fault |
|    7    |   0  |    2    |    3    |    0    | Page Fault |
|    8    |   4  |    4    |    3    |    0    | Page Fault |
|    9    |   2  |    4    |    2    |    0    | Page Fault |
|    10   |   3  |    4    |    2    |    3    | Page Fault |
|    11   |   0  |    0    |    2    |    3    | Page Fault |
|    12   |   3  |    0    |    2    |    3    | Page Hit   |
|    13   |   2  |    0    |    2    |    3    | Page Hit   |

2. **Tabel LRU**

| Langkah | Page | Frame 1 | Frame 2 | Frame 3 | Status     |
| ------- | ---- | ------- | ------- | ------- | ---------- |
|    1    |   7  |    7    |    -    |    -    | Page Fault |
|    2    |   0  |    7    |    0    |    -    | Page Fault |
|    3    |   1  |    7    |    0    |    1    | Page Fault |
|    4    |   2  |    0    |    1    |    2    | Page Fault |
|    5    |   0  |    1    |    2    |    0    | Page Hit   |
|    6    |   3  |    2    |    0    |    3    | Page Fault |
|    7    |   0  |    2    |    3    |    0    | Page Hit   |
|    8    |   4  |    3    |    0    |    4    | Page Fault |
|    9    |   2  |    0    |    4    |    2    | Page Fault |
|    10   |   3  |    4    |    2    |    3    | Page Fault |
|    11   |   0  |    2    |    3    |    0    | Page Fault |
|    12   |   3  |    2    |    0    |    3    | Page Hit   |
|    13   |   2  |    0    |    3    |    2    | Page Hit   |

3. **Perbandingan**

|Algoritma|	Jumlah Page Fault	|Keterangan|
|-----|-----|-----|
|FIFO|	10|	Mengganti halaman yang masuk paling awal.|
|LRU|	9|	Mengganti halaman yang paling lama tidak digunakan.|
---

## Kesimpulan
- Manajemen memori dengan teknik page replacement berperan penting dalam mengoptimalkan penggunaan RAM. 
- Algoritma FIFO mengganti page berdasarkan urutan masuk sehingga mudah diterapkan, namun kurang efisien. Sebaliknya, LRU mengganti page yang paling lama tidak digunakan sehingga lebih efektif mengurangi page fault, meskipun implementasinya lebih kompleks. Oleh karena itu, pemilihan algoritma page replacement harus disesuaikan dengan kebutuhan dan sumber daya sistem.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?

   **Jawaban:**  
   Perbedaan utama FIFO dan LRU terletak pada dasar penggantian page:

- FIFO (First In First Out) mengganti page yang paling lama masuk ke memori, tanpa memperhatikan apakah page tersebut sering digunakan atau tidak.

- LRU (Least Recently Used) mengganti page yang paling lama tidak digunakan, berdasarkan riwayat akses.

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?

   **Jawaban:**  

   FIFO dapat menghasilkan Belady’s Anomaly karena page diganti berdasarkan urutan masuk, bukan tingkat penggunaan, sehingga penambahan frame bisa justru meningkatkan jumlah page fault.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
 
   **Jawaban:**  
LRU umumnya lebih baik karena mengganti page yang paling lama tidak digunakan, sehingga lebih sesuai dengan pola akses program dan menghasilkan page fault lebih sedikit dibanding FIFO.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
Menghitung FIFO DAN LRU, membuat codingan dan banyak yang error. 
- Bagaimana cara Anda mengatasinya?  
Membenarkan dan teliti.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
