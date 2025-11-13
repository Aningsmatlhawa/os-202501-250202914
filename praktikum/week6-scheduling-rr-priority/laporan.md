
# Laporan Praktikum Minggu [6]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling


---

## Identitas
- **Nama**  : Ani Ngismatul Hawa 
- **NIM**   : 250202914
- **Kelas** : 1IKRB

---

## Tujuan
1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.


---

## Dasar Teori
- **Penjadwalan CPU** itu seperti sistem antrian tugas di komputer. Saat banyak program ingin dijalankan, CPU tidak bisa mengerjakan semuanya sekaligus, jadi sistem operasi mengatur urutannya.
penjadwalan CPU menentukan proses mana yang dikerjakan dulu, mana yang menunggu, dan berapa lama setiap proses mendapat giliran. Tujuannya biar komputer tetap cepat, adil, dan tidak ada tugas yang terlalu lama menunggu.
- **Round Robin** adalah cara penjadwalan CPU yang membagi waktu secara bergiliran dan adil untuk setiap proses.
Setiap proses diberi jatah waktu singkat yang disebut quantum. Kalau proses belum selesai saat waktunya habis, dia harus antre lagi di belakang barisan dan menunggu giliran berikutnya.
- **Priority Scheduling** adalah cara penjadwalan CPU yang memilih proses berdasarkan tingkat prioritasnya.
Artinya, proses yang punya prioritas lebih tinggi akan dijalankan lebih dulu, sedangkan yang prioritasnya rendah harus menunggu.
---

## Langkah Praktikum
1. Siapkan Data Proses
2. Eksperimen 1 Round Robin
- Gunakan time quantum (q) = 3.
- Hitung waiting time dan turnaround time untuk tiap proses.
- Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
- Catat sisa burst time tiap putaran.
3. Eksperimen 2 – Priority Scheduling (Non-Preemptive)
- urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
- Lakukan perhitungan manual untuk:

`WT[i] = waktu mulai eksekusi - Arrival[i]`
`TAT[i] = WT[i] + Burst[i]`
- Buat tabel perbandingan hasil RR dan Priority.
4. Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)

-  Ubah quantum menjadi 2 dan 5.
- Amati perubahan nilai rata-rata waiting time dan turnaround time.
- Buat tabel perbandingan efek quantum.
5. Eksperimen 4 – Dokumentasi

- Simpan semua hasil tabel dan screenshot ke:

`praktikum/week6-scheduling-rr-priority/screenshots/`

6. Commit & Push

`git add .`

`git commit -m "Minggu 6 - CPU Scheduling RR & Priority"`

`git push origin main`

---

## Kode / Perintah

- Data proses

|Proses|Burst Time|	Arrival Time|	Priority|
|-----|-------|-----|----|
|P1|	5|	0|	2|
|P2|3|	1|	1|
|P3|	8|	2|	4|
|P4|	6|	3|	3|

-  Gunakan time quantum (q) = 3.
-  Gantt Chart

`| P1 | P2 | P3 | P4 | P1 | P3 | ...`

`0    3    6    9   12   15   18  ...`

- Lakukan perhitungan manual untuk:

`WT[i] = waktu mulai eksekusi - Arrival[i]`
`TAT[i] = WT[i] + Burst[i]`

- Hasil perhitungan dan analisis dimasukkan ke `laporan.md.`
- Screenshot tabel atau Gantt Chart disimpan di folder `screenshots/.`
- Laporan lengkap berada di laporan.md.
- Semua hasil telah di-commit ke GitHub tepat waktu.

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/Hasil%206.png)
1. **Eksperimen 1 Round Robin**

![Screenshot hasil](./screenshots/Round%20Robin.png)
- Gantt Chart

 | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
0    3    6    9    12   14   17   20   22 

2. **Eksperimen 2 Priority Scheduling**

![Screenshot hasil](./screenshots/Priority.png)
- Gantt Chart

 | P1 | P2 | P4 | P3 |
0    5    8   14   22

3. **Perbandingan antara Round Robin & Priority Scedulling** :

|Algoritma|	Avg Waiting Time|	Avg Turnaround Time|	Kelebihan|	Kekurangan|
|---------|----------|--------|--------|-------|
|RR|	8,5	|14|	Adil terhadap semua proses	|Tidak efisien jika quantum tidak tepat|
|Priority	|5,25|	10,75|	Efisien untuk proses penting|	Potensi starvation pada prioritas rendah|
---

## Analisis
- **Round Robin (RR)**: Setiap proses dapat waktu sama (quantum 3). Hasilnya adil tapi waktu tunggu dan selesai rata-rata lebih lama (TAT 14, WT 8.5).

- **Priority Scheduling**: Proses dijalankan sesuai prioritas. Lebih cepat (TAT 10.75, WT 5.25) tapi tidak adil karena proses prioritas rendah bisa lama menunggu.

---

## Kesimpulan

Dari percobaan di atas, penjadwalan *Round Robin* memberikan waktu yang adil untuk semua proses tetapi membuat waktu tunggu dan selesai jadi lebih lama. Sedangkan *Priority Scheduling* lebih cepat karena menjalankan proses berdasarkan tingkat prioritas, meski proses prioritas rendah harus menunggu lebih lama. Jadi, Round Robin cocok untuk sistem yang butuh keadilan, sementara Priority Scheduling lebih efisien untuk menyelesaikan proses penting lebih dulu.


---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
   **Jawaban:**  
*Round Robin* memberi giliran sama untuk semua proses, sedangkan *Priority Scheduling* menjalankan proses berdasarkan tingkat pentingnya.

2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem? 

   **Jawaban:**  
Kalau time quantum terlalu kecil, CPU sering berganti proses, jadi sistem jadi lambat karena terlalu banyak waktu terbuang untuk pergantian (overhead).
Kalau terlalu besar, proses panjang bisa mendominasi CPU, sehingga sistem terasa tidak adil dan responnya lambat
3. Mengapa algoritma Priority dapat menyebabkan starvation?

   **Jawaban:**  
Algoritma Priority bisa menyebabkan starvation karena proses dengan prioritas rendah terus tertunda.
Kalau selalu ada proses dengan prioritas tinggi yang masuk, proses prioritas rendah tidak pernah mendapat giliran untuk dijalankan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
menghitung start dan finish setiap eksperimen.
- Bagaimana cara Anda mengatasinya?  
mengatasi dengan mempelajari dengan cermat.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
