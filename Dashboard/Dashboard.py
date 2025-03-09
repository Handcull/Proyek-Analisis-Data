import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === 🎯 LOAD DATASET ===
@st.cache_data
def load_data():
    df = pd.read_csv("Dashboard/day.csv")  
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Mist/Cloudy', 3: 'Light Rain/Snow'})
    df['weekday'] = df['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 
                                       4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})
    return df

df = load_data()

# === 📌 SIDEBAR FILTER ===
st.sidebar.header("🔍 Filter Data")
season_filter = st.sidebar.multiselect("Pilih Musim:", df['season'].unique(), default=df['season'].unique())
weather_filter = st.sidebar.multiselect("Pilih Kondisi Cuaca:", df['weathersit'].unique(), default=df['weathersit'].unique())

# Filter Data berdasarkan pilihan pengguna
df_filtered = df[(df['season'].isin(season_filter)) & (df['weathersit'].isin(weather_filter))]

# === 🎯 DASHBOARD TITLE ===
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Dashboard ini menampilkan **analisis peminjaman sepeda** berdasarkan berbagai faktor seperti musim, cuaca, dan hari dalam seminggu.")

# === 🔍 MENAMPILKAN DATA ===
st.subheader("📊 Dataset Peminjaman Sepeda")
with st.expander("📌 Lihat Data"):
    st.write(df_filtered.head())

# === 🔍 INSIGHT UTAMA ===
st.markdown("## 🔹 **Key Insights**")
st.markdown("- Peminjaman sepeda **meningkat** saat cuaca cerah.")
st.markdown("- Musim **Fall (Gugur)** memiliki tingkat peminjaman tertinggi.")
st.markdown("- Akhir pekan cenderung memiliki peminjaman **lebih tinggi** dibanding hari kerja.")

# === 📊 DISTRIBUSI JUMLAH PEMINJAMAN SEPEDA ===
st.subheader("📈 Distribusi Jumlah Peminjaman Sepeda")
st.markdown("Histogram ini menunjukkan distribusi jumlah peminjaman sepeda setiap harinya.")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(df_filtered['cnt'], bins=30, kde=True, color="blue", ax=ax)
plt.xlabel("Jumlah Peminjaman")
plt.ylabel("Frekuensi")
st.pyplot(fig)

# === 📊 TREN PEMINJAMAN BERDASARKAN BULAN ===
st.subheader("📅 Tren Peminjaman Sepeda Berdasarkan Bulan")
st.markdown("Boxplot ini menunjukkan variasi peminjaman sepeda berdasarkan bulan dalam setahun.")
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(x="mnth", y="cnt", data=df_filtered, palette="coolwarm", ax=ax)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# === 🌦️ HUBUNGAN KONDISI CUACA & JUMLAH PEMINJAMAN ===
st.subheader("🌦️ Hubungan Kondisi Cuaca dengan Jumlah Peminjaman")
st.markdown("Boxplot ini membandingkan jumlah peminjaman sepeda dalam berbagai kondisi cuaca.")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="weathersit", y="cnt", data=df_filtered, palette="Set2", ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# === 🏢 PERBANDINGAN HARI KERJA VS AKHIR PEKAN ===
st.subheader("🏢 Peminjaman pada Hari Kerja vs Akhir Pekan")
st.markdown("Visualisasi ini membandingkan jumlah peminjaman sepeda antara hari kerja dan akhir pekan.")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="workingday", y="cnt", data=df_filtered, palette="coolwarm", ax=ax)
plt.xlabel("Hari Kerja (1 = Ya, 0 = Tidak)")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# === 📆 RATA-RATA PEMINJAMAN SEPEDA BERDASARKAN HARI ===
st.subheader("📆 Rata-rata Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
st.markdown("Bar chart ini menunjukkan rata-rata peminjaman sepeda dari Senin hingga Minggu.")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="weekday", y="cnt", data=df_filtered, palette="coolwarm", errorbar=None, ax=ax)
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(fig)

# === 🔹 KESIMPULAN ===
st.markdown("## 📝 **Kesimpulan**")
st.markdown("- Cuaca yang lebih cerah meningkatkan jumlah peminjaman sepeda.")
st.markdown("- Tren peminjaman sepeda **lebih tinggi di musim gugur** dibanding musim lainnya.")
st.markdown("- Akhir pekan memiliki **tingkat peminjaman lebih tinggi** dibanding hari kerja.")

# === 🚀 END ===
st.success("🎉 Dashboard berhasil dimuat! Gunakan sidebar untuk melakukan filter data.")

