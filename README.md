# Data Warehouse Harga Beras Sumatera Utara

## 1. Deskripsi Proyek

Data Warehouse Harga Beras Sumatera Utara merupakan proyek pengelolaan dan analisis data harga beras yang bertujuan mengintegrasikan data dari beberapa wilayah ke dalam satu pusat penyimpanan data.

Proyek ini menggunakan pendekatan Extract, Transform, Load (ETL) untuk memindahkan dan mengolah data dari database sumber ke dalam Data Warehouse berbasis PostgreSQL.

Data yang telah terintegrasi kemudian dianalisis menggunakan Online Analytical Processing (OLAP) dan divisualisasikan untuk membantu memahami perkembangan harga beras di Sumatera Utara.

## 2. Tujuan Proyek

1. Mengintegrasikan data harga beras dari beberapa wilayah.
2. Membangun Data Warehouse menggunakan PostgreSQL.
3. Mengelola data berdasarkan dimensi wilayah, kualitas beras, dan waktu.
4. Melakukan analisis harga menggunakan OLAP.
5. Menyajikan hasil analisis melalui visualisasi data.

## 3. Cakupan Data

| Komponen | Keterangan |
|---|---|
| Wilayah | Gunung Sitoli, Padang Sidempuan, Pematang Siantar |
| Kategori kualitas | 7 kategori |
| Periode | Januari-November 2026 |
| Total observasi | 231 baris |
| Database | PostgreSQL |

## 4. Teknologi yang Digunakan

- Neon PostgreSQL
- Google Colab
- Python
- Pandas
- Matplotlib
- GitHub
- SQL

## 5. Arsitektur Data Warehouse

Proses pengolahan data terdiri dari:

1. Extract: mengambil data dari database sumber.
2. Transform: membersihkan dan menyiapkan data.
3. Load: memasukkan data ke dalam Data Warehouse.
4. OLAP: melakukan analisis berdasarkan dimensi wilayah, kualitas, dan waktu.
5. Visualization: menyajikan hasil analisis dalam bentuk grafik.

## 6. Struktur Data Warehouse

Data Warehouse menggunakan skema dimensional yang terdiri dari:

- dim_wilayah: menyimpan informasi wilayah.
- dim_kualitas_beras: menyimpan kategori kualitas beras.
- dim_tanggal: menyimpan informasi waktu.
- fact_harga_beras: menyimpan fakta harga beras.

## 7. Analisis OLAP

Analisis yang dilakukan meliputi:

1. Rata-rata harga beras berdasarkan wilayah.
2. Tren harga beras bulanan berdasarkan wilayah.
3. Analisis harga berdasarkan kualitas beras.
4. Drill-down harga berdasarkan wilayah, kualitas, dan tanggal.

Query analisis tersedia pada folder sql/.

## 8. Hasil Visualisasi

### Tren Harga Beras Bulanan

![Tren Harga Beras Bulanan](docs/images/tren_harga_bulanan.png)

### Perbandingan Harga Antarwilayah

![Perbandingan Harga Antarwilayah](docs/images/perbandingan_harga_antarwilayah.png)

## 9. Notebook

Notebook pengolahan data tersedia pada folder notebooks/:

- ETL_HARGA_BERAS_SUMUT.ipynb
- ETL_Perbaikan_Dua_Wilayah_Final.ipynb

## 10. Evaluasi

Dokumentasi evaluasi analisis OLAP tersedia pada:

docs/evaluasi_olap.md

## 11. Pengembang

Proyek ini dikembangkan sebagai proyek akademik Data Warehouse dengan fokus pada integrasi dan analisis data harga beras di Sumatera Utara.
