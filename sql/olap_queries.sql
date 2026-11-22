-- =====================================================
-- DATA WAREHOUSE HARGA BERAS SUMATERA UTARA
-- OLAP QUERIES
-- =====================================================

-- 1. Rata-rata harga beras berdasarkan wilayah
SELECT
    w.nama_wilayah,
    ROUND(AVG(f.harga), 2) AS rata_rata_harga
FROM dw.fact_harga_beras f
JOIN dw.dim_wilayah w
    ON f.wilayah_key = w.wilayah_key
GROUP BY w.nama_wilayah
ORDER BY rata_rata_harga DESC;


-- 2. Tren harga beras bulanan berdasarkan wilayah
SELECT
    t.tahun,
    t.bulan,
    t.nama_bulan,
    w.nama_wilayah,
    ROUND(AVG(f.harga), 2) AS rata_rata_harga
FROM dw.fact_harga_beras f
JOIN dw.dim_tanggal t
    ON f.tanggal_key = t.tanggal_key
JOIN dw.dim_wilayah w
    ON f.wilayah_key = w.wilayah_key
GROUP BY
    t.tahun,
    t.bulan,
    t.nama_bulan,
    w.nama_wilayah
ORDER BY t.tahun, t.bulan, w.nama_wilayah;


-- 3. Analisis harga berdasarkan kualitas beras
SELECT
    q.kualitas_beras,
    ROUND(AVG(f.harga), 2) AS rata_rata_harga,
    MIN(f.harga) AS harga_minimum,
    MAX(f.harga) AS harga_maksimum
FROM dw.fact_harga_beras f
JOIN dw.dim_kualitas_beras q
    ON f.kualitas_key = q.kualitas_key
GROUP BY q.kualitas_beras
ORDER BY rata_rata_harga DESC;


-- 4. Drill-down harga berdasarkan wilayah,
-- kualitas, dan tanggal
SELECT
    w.nama_wilayah,
    q.kualitas_beras,
    t.tanggal,
    f.kode_harga,
    f.harga
FROM dw.fact_harga_beras f
JOIN dw.dim_wilayah w
    ON f.wilayah_key = w.wilayah_key
JOIN dw.dim_kualitas_beras q
    ON f.kualitas_key = q.kualitas_key
JOIN dw.dim_tanggal t
    ON f.tanggal_key = t.tanggal_key
ORDER BY
    w.nama_wilayah,
    q.kualitas_beras,
    t.tanggal;
