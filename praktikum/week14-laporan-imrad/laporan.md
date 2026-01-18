
# Laporan Praktikum Minggu [14]

Topik: Penyusunan Laporan Praktikum Format IMRAD "Scheduling (FCFS/SJF)"
---

## Identitas
- **Nama**  : Ani Ngismatul Hawa  
- **NIM**   : 250202914  
- **Kelas** : 1IKRB

---
## Pendahuluan
### A. Latar Belakang
CPU scheduling merupakan mekanisme penting dalam sistem operasi untuk mengatur urutan eksekusi proses yang berjalan pada CPU. Penjadwalan yang tepat berpengaruh langsung terhadap efisiensi sistem, khususnya pada waktu tunggu dan waktu penyelesaian proses. Oleh karena itu, pemilihan algoritma penjadwalan menjadi hal yang krusial.

Algoritma First Come First Served (FCFS) dan Shortest Job First (SJF) merupakan dua algoritma dasar dalam penjadwalan CPU. FCFS mengeksekusi proses berdasarkan urutan kedatangan, sedangkan SJF memprioritaskan proses dengan waktu eksekusi terpendek. Melalui praktikum ini, dilakukan perhitungan dan perbandingan kedua algoritma tersebut untuk memahami perbedaan kinerja serta kelebihan dan kekurangan masing-masing dalam pengelolaan proses CPU.

### B. Tujuan
> Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.

> Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.

> Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.

>Menjelaskan kelebihan dan kekurangan masing-masing algoritma.

> Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.

---
## Metode
### A. Data Proses

|Proses|	Burst Time|	Arrival Time|
|----|------|-----|
|P1|	6|	0|
|P2|	8|	1|
|P3|	7|	2|
|P4|	3|	3|

---
### B. Langkah Eksperimen
1. Menyiapkan data proses yang terdiri dari Process ID, Arrival Time, dan Burst Time.

2. Menentukan urutan eksekusi proses menggunakan algoritma FCFS berdasarkan waktu kedatangan.

3. Menghitung waiting time dan turnaround time untuk setiap proses pada algoritma FCFS.

4. Menentukan urutan eksekusi proses menggunakan algoritma SJF berdasarkan burst time terpendek.

5. Menghitung waiting time dan turnaround time untuk setiap proses pada algoritma SJF.

6. Membandingkan hasil perhitungan FCFS dan SJF dalam bentuk tabel untuk menganalisis perbedaan kinerja.
---

## Hasil
### A. Hasil FCFS
![Screenshot hasil](./screenshots/FCFS.png)

### B. Hasil SJF
![Screenshot hasil](./screenshots/SJF.png)

### C. Hasil Perbandingan *FCFS* dan *SJF* 
![Screenshot hasil](./screenshots/Hasil.png)

### D. Tabel Analisis Perbandingan

|Algoritma	|Avg Waiting Time	|Avg Turnaround Time	|Kelebihan	|Kekurangan|
|-----|-----|----|-----|----|
|FCFS|	8,75|	14,75|Sederhana dan mudah diterapkan|Tidak efisien untuk proses panjang|
|SJF|	6,25|	12,25|Optimal untuk job pendek|Menyebabkan starvation pada job panjang|

---

## Pembahasan
Hasil eksperimen menunjukkan bahwa algoritma FCFS mengeksekusi proses berdasarkan urutan kedatangan sehingga proses dengan waktu eksekusi panjang dapat meningkatkan waktu tunggu proses lain. Sebaliknya, algoritma SJF lebih efisien karena memprioritaskan proses dengan burst time terpendek, yang berdampak pada rata-rata waiting time dan turnaround time yang lebih kecil. Namun, SJF berpotensi menyebabkan proses berdurasi panjang harus menunggu lebih lama, sehingga pemilihan algoritma penjadwalan perlu disesuaikan dengan kondisi dan kebutuhan sistem.

---

## Kesimpulan
1. Penjadwalan CPU berperan penting dalam menentukan efisiensi eksekusi proses pada sistem operasi.

2. FCFS mengutamakan urutan kedatangan proses, namun kurang optimal ketika proses memiliki waktu eksekusi yang bervariasi.

3. SJF lebih efektif dalam menekan waktu tunggu proses, meskipun berisiko menunda proses berdurasi panjang.

---

---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?  
   **Jawaban:** 

   Format IMRAD membuat laporan lebih ilmiah karena menyajikan penelitian secara terstruktur dari tujuan, metode, hasil, hingga pembahasan, sehingga mudah dipahami, direplikasi, dan dievaluasi.

2. Apa perbedaan antara bagian Hasil dan Pembahasan? 
   **Jawaban:**  

   Bagian **Hasil** menyajikan data atau temuan eksperimen secara objektif, sedangkan **Pembahasan** menjelaskan, menganalisis, dan menafsirkan hasil tersebut.

3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum? 
   **Jawaban:**  
   Sitasi dan daftar pustaka penting untuk menghargai sumber asli, menghindari plagiarisme, dan memperkuat keabsahan laporan praktikum dengan dasar teori yang jelas.


---
## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th ed.). Wiley.

2. Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems (4th ed.). Pearson Education.

3. Arpaci-Dusseau, R. H., & Arpaci-Dusseau, A. C. (2018). Operating Systems: Three Easy Pieces. Arpaci-Dusseau Books.

---
## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
