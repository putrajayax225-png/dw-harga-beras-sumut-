# Evaluasi OLAP Data Warehouse Harga Beras Sumatera Utara

## 1. Pendahuluan

Evaluasi OLAP dilakukan untuk menguji kemampuan Data Warehouse dalam menyimpan, mengintegrasikan, dan menyajikan data harga beras berdasarkan dimensi wilayah, kualitas beras, dan waktu.

## 2. Sumber Data

Data yang digunakan berasal dari database pusat harga beras Sumatera Utara dan dimuat ke dalam Data Warehouse PostgreSQL menggunakan proses ETL.

Cakupan data:
- Wilayah: Gunung Sitoli, Padang Sidempuan, dan Pematang Siantar.
- Kategori kualitas: 7 kategori kualitas beras.
- Periode pengamatan: Januari-November 2026.
- Jumlah data: 231 baris.

## 3. Hasil Analisis OLAP

### 3.1 Analisis Harga Berdasarkan Wilayah

Analisis ini digunakan untuk mengetahui rata-rata harga beras pada masing-masing wilayah.

### 3.2 Analisis Tren Harga Bulanan

Analisis ini digunakan untuk mengamati perubahan rata-rata harga beras setiap bulan berdasarkan wilayah.

### 3.3 Analisis Berdasarkan Kualitas Beras

Analisis ini digunakan untuk membandingkan rata-rata, harga minimum, dan harga maksimum berdasarkan kategori kualitas beras.

### 3.4 Drill-Down Analysis

Analisis ini menampilkan informasi harga secara lebih terperinci berdasarkan wilayah, kualitas beras, dan tanggal pengamatan.

## 4. Visualisasi Data

Visualisasi yang digunakan meliputi:

1. Grafik tren harga beras bulanan berdasarkan wilayah.
2. Grafik perbandingan rata-rata harga beras antarwilayah.

## 5. Kesimpulan

Analisis OLAP membantu menyajikan informasi harga beras berdasarkan berbagai dimensi sehingga data dapat digunakan untuk mendukung pemantauan dan analisis perkembangan harga beras di Sumatera Utara.
