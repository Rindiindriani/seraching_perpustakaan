import streamlit as st
import json
import os

# Fungsi untuk membaca file JSON
def baca_data_dari_file(nama_file):
    if os.path.exists(nama_file):
        with open(nama_file, 'r') as file:
            data = json.load(file)
        return data
    else:
        st.error(f"File '{nama_file}' tidak ditemukan.")
        return None

# Fungsi untuk melakukan pencarian berdasarkan judul buku
def cari_buku(judul_dicari, data):
    for buku in data:
        if buku['judul'].lower() == judul_dicari.lower():
            return buku
    return None

# Nama file JSON yang ingin dibaca
nama_file = 'C:\\Users\\rindi\\Downloads\\datajsonbuku.json'

# Pengaturan tampilan
st.set_page_config(
    page_title="Pencarian Buku Perpustakaan",
    layout="wide"
)

# Sidebar
st.sidebar.header("Pencarian Buku")
st.sidebar.markdown("""
Gunakan aplikasi ini untuk mencari lokasi buku di perpustakaan.  
Pilih judul buku pada kolom di bawah dan tekan tombol 'Cari'.
""")

# Judul aplikasi
st.title("📚 Pencarian Buku Perpustakaan")

# Membaca data dari file JSON
data_buku = baca_data_dari_file(nama_file)

# Jika data buku berhasil dibaca
if data_buku:
    # Ambil daftar judul buku dan tambahkan pilihan default
    daftar_judul = ["Pilih judul buku"] + [buku['judul'] for buku in data_buku]
    # Input dari pengguna
    judul_yang_dicari = st.selectbox("Pilih Judul Buku:", daftar_judul)

    # Tombol untuk mencari
    if st.button("Cari"):
        if judul_yang_dicari != "Pilih judul buku":
            hasil_pencarian = cari_buku(judul_yang_dicari, data_buku)
            if hasil_pencarian:
                st.success("Buku yang ditemukan:")
                st.write(f"*Judul:* {hasil_pencarian['judul']}")
                st.write(f"*Lokasi:* Lantai {hasil_pencarian['lantai']}, Ruangan {hasil_pencarian['ruangan']}, Nomor Rak {hasil_pencarian['rak']}")
            else:
                st.warning("Tidak ada buku yang ditemukan dengan judul tersebut.")
        else:
            st.warning("Silakan pilih judul buku.")
else:
    st.error("Data buku tidak tersedia.")
