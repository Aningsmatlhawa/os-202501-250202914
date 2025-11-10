
# Laporan Praktikum Minggu [5]
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Ani Ngismatul Hawa  
- **NIM**   : 250202914
- **Kelas** : 1IKRB

---

## Tujuan

1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.

---

## Dasar Teori
- CPU

CPU adalah otak utama komputer yang bertugas menjalankan perintah dan mengolah data dari perangkat lunak. Semua proses dalam komputer, seperti menjalankan program, menghitung data, dan mengatur aliran informasi, dilakukan oleh CPU.
- FCFS (First Come, First Served)

FCFS adalah algoritma penjadwalan yang mengeksekusi proses berdasarkan urutan kedatangannya. Proses yang datang lebih dulu akan dijalankan lebih dulu tanpa bisa diganggu sebelum selesai. Cara ini sederhana dan bekerja seperti sistem antrian, namun bisa membuat proses yang datang belakangan menunggu lama jika proses pertama berjalan lama.

- SJF (Shortest Job First)

SJF adalah algoritma yang memilih proses dengan waktu eksekusi paling singkat untuk dijalankan lebih dulu. Tujuannya agar waktu tunggu semua proses jadi lebih efisien. Algoritma ini bisa bersifat non-preemptive atau preemptive (SRTF), tergantung apakah proses yang sedang berjalan bisa digantikan oleh proses baru yang lebih pendek.

---

## Langkah Praktikum
1. Siapkan Data Proses

2. Eksperimen 1 – FCFS (First Come First Served)

- Urutkan proses berdasarkan Arrival Time.
- Hitung nilai berikut untuk tiap proses:
> Waiting Time (WT) = waktu mulai eksekusi - Arrival Time

> Turnaround Time (TAT) = WT + Burst Time

- Hitung rata-rata Waiting Time dan Turnaround Time.
- Buat Gantt Chart sederhana:

3. Eksperimen 2 – SJF (Shortest Job First)

- Urutkan proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu kedatangan).

- Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.
- lakukan perbandingan

4. Eksperimen 3 – Visualisasi Spreadsheet (Opsional)

- Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
- Gunakan formula dasar penjumlahan/subtraksi.


---

## Kode / Perintah
1. 
|Proses	|Burst Time	|Arrival Time|
|--------|-----------|------------|
|P1|	6	|0|
|P2|8|1|
|P3	|7	|2|
|P4|	3|	3|

2. FCFS

`Waiting Time (WT) = waktu mulai eksekusi- Arrival Time`

`Turnaround Time (TAT) = WT + Burst Time`

3. Buat Chant Sederhana 

| P1 | P2 | P3 | P4 |
0    6    14   21   24

4. push

`git add .
git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
git push origin main`


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Hasil.png)
1. Eksperimen 1 – FCFS (First Come First Served)
![Screenshot hasil](./screenshots/FCFS.png)

- Gantt Chart sederhana

| P1 | P2 | P3 | P4 |

0    6    14   21   24

2. Eksperimen 2 – SJF (Shortest Job First)
![Screenshot hasil](./screenshots/SJF.png)

|Algoritma	|Avg Waiting Time|	Avg Turnaround Time	|Kelebihan	|Kekurangan|
|------|------|------|-----|-----|
|FCFS	|8,75	|14,75|	Sederhana dan mudah diterapkan|	Tidak efisien untuk proses panjang|
|SJF|	6,25	|12,25|	Optimal untuk job pendek|	Menyebabkan starvation pada job panjang|

- Gantt Chart sederhana

| P1 | P2 | P3 | P4 |

0    6    19   16   24

---

## Analisis

1. Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.

SJF memiliki nilai rata-rata waktu tunggu (WT) dan waktu penyelesaian (TAT) lebih kecil dibanding FCFS. Ini berarti SJF bekerja lebih efisien dalam mengatur proses, karena total waktu tunggu dan penyelesaiannya lebih cepat.

2. Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.

- SJF lebih unggul saat proses memiliki burst time (lama eksekusi) yang berbeda-beda, karena algoritma ini mendahulukan proses yang lebih cepat sehingga total waktu tunggu berkurang.

- FCFS lebih baik digunakan jika semua proses memiliki burst time yang hampir sama atau saat sistem menekankan urutan kedatangan (fairness), karena FCFS tidak memerlukan perkiraan waktu proses.

---

## Kesimpulan
Secara umum, SJF lebih efisien dibanding FCFS dalam hal waktu tunggu dan waktu penyelesaian rata-rata, terutama jika waktu eksekusi proses berbeda-beda. Namun, FCFS lebih sederhana dan adil terhadap urutan kedatangan proses

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
   **Jawaban:**  
   Perbedaan utamanya:

* **FCFS**: proses dikerjakan sesuai urutan datang.
* **SJF**: proses dengan waktu kerja paling cepat dikerjakan duluan.

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?

   **Jawaban:**  

   Karena SJF mengerjakan proses paling cepat dulu, jadi antrian lebih efisien dan waktu tunggu rata-rata jadi paling kecil.

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?

   **Jawaban:**  
Kelemahan SJF di sistem interaktif adalah sulit menebak waktu proses yang akan datang, dan bisa membuat proses panjang terus tertunda kalau banyak proses pendek muncul terus.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
bingung saat mempelajari excel dan dalam menghitung agak salah
- Bagaimana cara Anda mengatasinya?  
mempelajari excel dengan benar dan meneliti dengan benar
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
