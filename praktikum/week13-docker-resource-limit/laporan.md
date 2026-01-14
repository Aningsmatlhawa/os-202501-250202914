
# Laporan Praktikum Minggu [13]
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Ani Ngismatul Hawa 
- **NIM**   : 250202914
- **Kelas** : 1IKRB

---

## Tujuan
> Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.

>Membangun image dan menjalankan container.

>Menjalankan container dengan pembatasan CPU dan memori.

>Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.

>Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
1. Docker dan Containerization: platform yang digunakan untuk menjalankan aplikasi dalam bentuk container
2. Resource Management pada Sistem Operasi: mengatur penggunaan sumber daya seperti CPU dan memori agar setiap proses berjalan secara adil dan tidak saling mengganggu.
3. Control Groups (cgroups): Cgroups adalah fitur kernel Linux yang memungkinkan pembatasan, pemantauan, dan pengelompokan penggunaan resource oleh suatu proses.
4. Pembatasan CPU pada Docker: Bertujuan untuk mengatur porsi waktu CPU yang dapat digunakan oleh container.
5. Pembatasan Memori pada Docker: Pembatasan memori digunakan untuk mengontrol jumlah RAM maksimum yang boleh digunakan container.
6. Dampak Resource Limit terhadap Aplikasi: Penerapan resource limit memberikan dampak langsung pada performa aplikasi

---

## Langkah Praktikum
1. Persiapan Lingkungan

- Pastikan Docker terpasang dan berjalan.
- Verifikasi:
```docker version```
```docker ps```
2. Membuat Aplikasi/Skrip Uji

Buat program sederhana di folder code/ (bahasa bebas) yang:

- Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
- Mengalokasikan memori bertahap (untuk mengamati limit memori).
3. Membuat Dockerfile

- Tulis Dockerfile untuk menjalankan program uji.
- Build image:
```docker build -t week13-resource-limit .```
4. Menjalankan Container Tanpa Limit

- Jalankan container normal:
```docker run --rm week13-resource-limit```
- Catat output/hasil pengamatan.
5. Menjalankan Container Dengan Limit Resource

- Jalankan container dengan batasan resource (contoh):

```docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit```
- Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. Monitoring Sederhana

- Jalankan container (tanpa --rm jika perlu) dan amati penggunaan resource:
```docker stats```
- Ambil screenshot output eksekusi dan/atau docker stats.
7. Commit & Push

```git add .```
```git commit -m "Minggu 13 - Docker Resource Limit"```
```git push origin main```


---

## Kode / Perintah
1. Tuliskan potongan kode atau perintah utama:
```docker version ```

```docker ps``` 

```docker build -t week13-resource-limit .```

```docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit```

```docker stats```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/docker%20build.png)
![Screenshot hasil](./screenshots/docker%20run.png)
![Screenshot hasil](./screenshots/dr2.png)
![Screenshot hasil](./screenshots/dr3.png)
![Screenshot hasil](./screenshots/dr4.png)
![Screenshot hasil](./screenshots/dengan%20limit.png)
![Screenshot hasil](./screenshots/dl2.png)
![Screenshot hasil](./screenshots/dl3.png)
![Screenshot hasil](./screenshots/dl4.png)
![Screenshot hasil](./screenshots/docker%20status.png)
---

## Analisis
Percobaan menunjukkan bahwa pembatasan resource pada Docker sangat mempengaruhi kinerja aplikasi. Tanpa limit, container dapat menggunakan CPU dan memori secara bebas sehingga program berjalan normal. Dengan adanya limit CPU, proses menjadi lebih lambat karena waktu eksekusi dibatasi. Sementara itu, pembatasan memori menyebabkan aplikasi berhenti atau mengalami error saat penggunaan memori melebihi batas. Hal ini membuktikan bahwa Docker resource limit efektif dalam mengontrol penggunaan sumber daya dan menjaga kestabilan sistem. 

---

## Kesimpulan
Docker resource limit merupakan fitur penting untuk mengatur pemakaian CPU dan memori pada container. Dengan pembatasan ini, aplikasi dapat berjalan lebih terkendali, sistem lebih stabil, dan penggunaan resource menjadi lebih efisien.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori? 

   **Jawaban:**  
   Container perlu dibatasi CPU dan memori agar penggunaan sumber daya sistem tetap terkendali. Pembatasan ini mencegah satu container menggunakan CPU atau memori secara berlebihan yang dapat mengganggu container lain maupun sistem host.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?

   **Jawaban:**  
   Perbedaan VM dan container dalam konteks isolasi resource adalah bahwa VM memiliki isolasi penuh karena setiap VM menjalankan sistem operasi sendiri di atas hypervisor, sehingga penggunaan resource lebih terpisah namun lebih berat. Sedangkan container berbagi kernel sistem operasi host, sehingga lebih ringan dan cepat, dengan isolasi resource yang diatur menggunakan mekanisme seperti *cgroups*.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?

   **Jawaban:** 
   **Dampak limit memori terhadap aplikasi yang boros memori:**

* Aplikasi menjadi lambat karena sering gagal mengalokasikan memori.
* Aplikasi bisa crash / berhenti sendiri (*out of memory*).
* Pada container, proses bisa langsung dihentikan (OOMKilled) oleh sistem.
* Data yang sedang diproses bisa hilang atau tidak selesai.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
