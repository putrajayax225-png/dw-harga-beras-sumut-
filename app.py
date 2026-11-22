import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Rice Price Intelligence",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Rice Price Intelligence")
st.subheader("Dashboard Data Warehouse Harga Beras Sumatera Utara")
st.caption("Sumber data: DW_HARGA_BERAS_SUMUT | PostgreSQL")

# ==========================================
# 2. KONEKSI DATABASE
# ==========================================

def get_connection():
    try:
        database_url = st.secrets["DATABASE_URL"]
        return psycopg2.connect(
            database_url,
            connect_timeout=15,
            sslmode="require"
        )
    except Exception as e:
        st.error("Koneksi database gagal. Periksa konfigurasi Secrets.")
        st.stop()

# ==========================================
# 3. FUNGSI MEMBACA DATA
# ==========================================

@st.cache_data(ttl=300)
def load_data():
    conn = get_connection()

    query = """
    SELECT
        f.kode_harga,
        w.nama_wilayah,
        q.kualitas_beras,
        t.tanggal,
        t.tahun,
        t.bulan,
        t.nama_bulan,
        f.harga
    FROM dw.fact_harga_beras f
    JOIN dw.dim_wilayah w
        ON f.wilayah_key = w.wilayah_key
    JOIN dw.dim_kualitas_beras q
        ON f.kualitas_key = q.kualitas_key
    JOIN dw.dim_tanggal t
        ON f.tanggal_key = t.tanggal_key
    ORDER BY t.tanggal
    """

    try:
        df = pd.read_sql_query(query, conn)
    finally:
        conn.close()

    return df

df = load_data()

# ==========================================
# 4. FILTER DATA
# ==========================================

st.sidebar.header("Filter Data")

wilayah_list = ["Semua Wilayah"] + sorted(
    df["nama_wilayah"].dropna().unique().tolist()
)

pilih_wilayah = st.sidebar.selectbox(
    "Pilih Wilayah",
    wilayah_list
)

kualitas_list = ["Semua Kualitas"] + sorted(
    df["kualitas_beras"].dropna().unique().tolist()
)

pilih_kualitas = st.sidebar.selectbox(
    "Pilih Kualitas Beras",
    kualitas_list
)

filtered_df = df.copy()

if pilih_wilayah != "Semua Wilayah":
    filtered_df = filtered_df[
        filtered_df["nama_wilayah"] == pilih_wilayah
    ]

if pilih_kualitas != "Semua Kualitas":
    filtered_df = filtered_df[
        filtered_df["kualitas_beras"] == pilih_kualitas
    ]

# ==========================================
# 5. RINGKASAN DATA
# ==========================================

st.header("Ringkasan Harga Beras")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Observasi",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Rata-rata Harga",
    f"Rp {filtered_df['harga'].mean():,.0f}"
    if not filtered_df.empty else "-"
)

col3.metric(
    "Harga Tertinggi",
    f"Rp {filtered_df['harga'].max():,.0f}"
    if not filtered_df.empty else "-"
)

col4.metric(
    "Harga Terendah",
    f"Rp {filtered_df['harga'].min():,.0f}"
    if not filtered_df.empty else "-"
)

# ==========================================
# 6. GRAFIK TREN HARGA BULANAN
# ==========================================

st.divider()
st.header("Tren Harga Beras Bulanan")

if not filtered_df.empty:
    tren = (
        filtered_df.groupby(
            ["tahun", "bulan", "nama_bulan", "nama_wilayah"],
            as_index=False
        )["harga"].mean()
    )

    tren["periode"] = (
        tren["nama_bulan"].astype(str)
        + " "
        + tren["tahun"].astype(str)
    )

    tren["periode_urut"] = (
        tren["tahun"] * 100 + tren["bulan"]
    )

    tren = tren.sort_values("periode_urut")

    fig_tren = px.line(
        tren,
        x="periode",
        y="harga",
        color="nama_wilayah",
        markers=True,
        title="Perkembangan Rata-rata Harga Beras"
    )

    fig_tren.update_layout(
        xaxis_title="Periode",
        yaxis_title="Harga (Rp)",
        legend_title="Wilayah"
    )

    st.plotly_chart(fig_tren, use_container_width=True)

# ==========================================
# 7. PERBANDINGAN HARGA ANTARWILAYAH
# ==========================================

st.header("Perbandingan Harga Antarwilayah")

if not filtered_df.empty:
    perbandingan = (
        filtered_df.groupby(
            "nama_wilayah",
            as_index=False
        )["harga"].mean()
    )

    fig_bar = px.bar(
        perbandingan,
        x="nama_wilayah",
        y="harga",
        text_auto=".2s",
        title="Rata-rata Harga Beras Berdasarkan Wilayah"
    )

    fig_bar.update_layout(
        xaxis_title="Wilayah",
        yaxis_title="Rata-rata Harga (Rp)"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

# ==========================================
# 8. TABEL DATA HARGA
# ==========================================

st.divider()
st.header("Data Harga Beras")

st.dataframe(
    filtered_df[
        [
            "kode_harga",
            "nama_wilayah",
            "kualitas_beras",
            "tanggal",
            "harga"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

# ==========================================
# 9. INFORMASI DATA
# ==========================================

st.caption(
    "Rice Price Intelligence | "
    "Data Warehouse Harga Beras Sumatera Utara"
)
