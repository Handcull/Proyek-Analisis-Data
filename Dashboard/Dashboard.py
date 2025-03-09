import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")  # Pastikan dataset ada di folder yang sama
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Mist/Cloudy', 3: 'Light Rain/Snow'})
    df['weekday'] = df['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 
                                       4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})
    return df

df = load_data()

# Sidebar Filter
st.sidebar.header("Filter Data")
season_filter = st.sidebar.multiselect("Pilih Musim", df['season'].unique(), default=df['season'].unique())
weather_filter = st.sidebar.multiselect("Pilih Kondisi Cuaca", df['weathersit'].unique(), default=df['weathersit'].unique())

# Filter Data
df_filtered = df[(df['season'].isin(season_filter)) & (df['weathersit'].isin(weather_filter))]

# Tampilkan Data
st.title("🚲 Bike Sharing Dashboard")
st.subheader("Dataset Peminjaman Sepeda")
st.write(df_filtered.head())

# Distribusi Jumlah Peminjaman Sepeda
st.subheader("Distribusi Jumlah Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8,5))
sns.histplot(df_filtered['cnt'], bins=30, kde=True, color="blue", ax=ax)
plt.xlabel("Jumlah Peminjaman")
plt.ylabel("Frekuensi")
st.pyplot(fig)

# Tren Peminjaman Berdasarkan Bulan
st.subheader("Tren Peminjaman Berdasarkan Bulan")
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(x="mnth", y="cnt", data=df_filtered, palette="coolwarm", ax=ax)
plt.xlabel("Bulan")
plt.ylabel("Jumlah Peminjaman Sepeda (Normalized)")
st.pyplot(fig)

# Hubungan Cuaca dan Jumlah Peminjaman
st.subheader("Hubungan Kondisi Cuaca dengan Jumlah Peminjaman")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="weathersit", y="cnt", data=df_filtered, palette="Set2", ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Peminjaman Sepeda (Normalized)")
st.pyplot(fig)

# Perbandingan Hari Kerja vs Akhir Pekan
st.subheader("Peminjaman pada Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(x="workingday", y="cnt", data=df_filtered, palette="coolwarm", ax=ax)
plt.xlabel("Hari Kerja (1 = Ya, 0 = Tidak)")
plt.ylabel("Jumlah Peminjaman Sepeda (Normalized)")
st.pyplot(fig)

# Rata-rata Peminjaman Sepeda Berdasarkan Hari dalam Seminggu
st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Hari dalam Seminggu")
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x="weekday", y="cnt", data=df_filtered, palette="coolwarm", errorbar=None, ax=ax)
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Jumlah Peminjaman Sepeda (Normalized)")
st.pyplot(fig)
