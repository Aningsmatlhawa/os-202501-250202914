
# Laporan Praktikum Minggu [11]
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Ani Ngismatul Hawa 
- **NIM**   : 250202914
- **Kelas** : 1IKRB

---

## Tujuan

> -  program sederhana untuk mendeteksi deadlock.
> - Menjalankan simulasi deteksi deadlock dengan dataset uji.
> - Menyajikan hasil analisis deadlock dalam bentuk tabel.
> - Memberikan interpretasi hasil uji secara logis dan sistematis.
> - Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
- Deadlock adalah kondisi ketika beberapa proses saling menunggu sumber daya satu sama lain sehingga tidak ada proses yang bisa berjalan. Akibatnya, sistem seperti “macet”.

- Simulasi deadlock digunakan untuk menggambarkan bagaimana deadlock bisa terjadi. Dengan simulasi, kita dapat melihat urutan permintaan dan penggunaan sumber daya oleh proses, sehingga lebih mudah memahami penyebab deadlock tanpa harus menunggu kejadian nyata di sistem.

---

## Langkah Praktikum

## 1. Menyiapkan Dataset

Gunakan dataset sederhana yang berisi:

- Daftar proses
- Resource Allocation
- Resource Request / Need

```Contoh tabel:```

|Proses|	Allocation|	Request|
|----|----|---|
|P1|	R1 |R2|
|P2|	R2	|R3|
|P3|	R3	|R1|

## 2. Implementasi Algoritma Deteksi Deadlock

Program minimal harus:

- Membaca data proses dan resource.
- Menentukan apakah sistem berada dalam kondisi deadlock.
- Menampilkan proses mana saja yang terlibat deadlock.
## 3. Eksekusi & Validasi

- Jalankan program dengan dataset uji.
- Validasi hasil deteksi dengan analisis manual/logis.
- Simpan hasil eksekusi dalam bentuk screenshot.
## 4. Analisis Hasil

- Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
- Jelaskan mengapa deadlock terjadi atau tidak terjadi.
- Kaitkan hasil dengan teori deadlock (empat kondisi).
## 5. Commit & Push

> ```git add .```
> ```git commit -m "Minggu 11 - Deadlock Detection"```
> ```git push origin main```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
## 1. Tabel 

|Proses|	Allocation|	Request|
|----|----|---|
|P1|	R1 |R2|
|P2|	R2	|R3|
|P3|	R3	|R1|



---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/Deadlock.png)
---

## Analisis
## Tabel Analisis Hasil

|Proses	|Status|
|---|----|
|P1	|Deadlock|
|P2	|Deadlock|
|P3	|Deadlock|
---

## Kesimpulan
- Sistem terbukti mengalami deadlock. Hal ini terjadi karena setiap proses memegang satu resource dan pada saat yang sama menunggu resource lain yang sedang digunakan oleh proses lain. Akibatnya, semua proses saling menunggu dan tidak ada yang bisa berjalan.

- Hasil dari program yang dijalankan sesuai dengan analisis secara logika, yaitu proses P1, P2, dan P3 semuanya terjebak deadlock. Kondisi ini menunjukkan bahwa sistem memenuhi syarat terjadinya deadlock, terutama adanya lingkaran tunggu antar proses. Dengan praktik ini, dapat dipahami bahwa deadlock bisa terjadi jika pengelolaan resource tidak diatur dengan baik.
---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?

   **Jawaban:**  

- Deadlock Prevention: Mencegah deadlock dari awal dengan aturan ketat.

- Deadlock Avoidance: Menghindari deadlock dengan perhitungan kondisi aman.

- Deadlock Detection: Membiarkan deadlock terjadi lalu mendeteksinya dan memperbaiki.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?

   **Jawaban:**  
Deteksi deadlock tetap diperlukan karena tidak semua deadlock bisa dicegah atau dihindari.
Dengan deteksi deadlock, sistem dapat menemukan kondisi macet yang sudah terjadi dan mengambil tindakan (misalnya menghentikan proses), sehingga sistem bisa kembali berjalan normal.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?  
   **Jawaban:**  
**A. Kelebihan deteksi deadlock:**

* Resource digunakan lebih efisien
* Tidak membatasi proses sejak awal
* Cocok untuk sistem yang kompleks

**B. Kekurangan deteksi deadlock:**

* Deadlock boleh terjadi terlebih dahulu
* Sistem bisa macet sementara
* Perlu biaya tambahan untuk mendeteksi dan memulihkan

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
