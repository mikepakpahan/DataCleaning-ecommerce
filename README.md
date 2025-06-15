# 📈 Analisis Kinerja & Dashboard E-Commerce

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-2.2.2-purple?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-5.22.0-blueviolet?style=for-the-badge&logo=plotly)

Selamat datang di ruang mesin analisis saya! Proyek ini adalah sebuah perjalanan untuk mengubah data mentah kinerja produk e-commerce menjadi sebuah dashboard analitis yang interaktif dan penuh wawasan.

### 📸 Demo Dashboard

![Screenshot 2025-06-15 144308](https://github.com/user-attachments/assets/119d223c-3bcc-45f7-82f5-56492ea734e0)

![image](https://github.com/user-attachments/assets/79138859-a0c0-449a-a1f6-e1d5632bc6c9)

---

### 📝 Tentang Proyek Ini

Proyek ini bertujuan untuk melakukan analisis data eksplorasi (EDA) secara mendalam pada dataset e-commerce untuk mengungkap pola dan strategi bisnis yang tersembunyi (sebenarnya untuk nyelesain tugas projek semester aja sih, Praktikum Sistem Informasi Manajemen). Semua wawasan yang ditemukan kemudian disajikan dalam sebuah aplikasi web interaktif yang dibangun menggunakan Streamlit, berfungsi sebagai alat bantu pengambilan keputusan strategis.

### ✨ Fitur Utama & Wawasan Kunci

Proyek ini berhasil mengungkap beberapa wawasan krusial:

* ✅ **Analisis Profitabilitas:** Mengidentifikasi **'Outerwear & Coats'** sebagai kategori produk dengan kontribusi profit total terbesar.
* ✅ **Analisis Siklus Penjualan:** Menemukan bahwa produk yang paling cepat laku (**'Clothing Sets'**) bukanlah produk yang paling menguntungkan, menunjukkan adanya dinamika antara produk *Fast Moving* dan *High Margin*.
* ✅ **Analisis Performa Merek:** Mengungkap dual-strategi **"Volume vs. Value"**, di mana merek terlaris tidak identik dengan merek paling profitabel.
* ✅ **Analisis Tren Waktu:** Memvisualisasikan **pertumbuhan bisnis yang eksponensial** dari tahun 2019 hingga 2024, dengan indikasi adanya pola musiman pada akhir tahun.
* ✅ **Dashboard Interaktif:** Menyajikan semua temuan dalam dashboard yang dinamis, memungkinkan pengguna untuk memfilter dan menjelajahi data secara mandiri.

---

### 🛠️ Teknologi yang Digunakan

* **Python:** Sebagai bahasa pemrograman utama.
* **Pandas:** Untuk manipulasi dan pembersihan data (Data Wrangling).
* **Plotly Express:** Untuk membuat visualisasi data yang interaktif dan modern.
* **Streamlit:** Untuk membangun dan menerapkan aplikasi web data (dashboard).
* **Lingkungan:** Google Colab untuk analisis awal, VS Code untuk pengembangan aplikasi.

---

### 🚀 Cara Menjalankan Proyek Ini

Untuk menjalankan dashboard ini di komputermu, ikuti langkah-langkah berikut:

1.  **Clone Repositori Ini**
    ```sh
    git clone github.com/mikepakpahan/DataCleaning-ecommerce.git
    cd DataCleaning-ecommerce
    ```

2.  **Buat dan Aktifkan Lingkungan Virtual (Virtual Environment)**
    ```sh
    # Buat venv
    python -m venv venv

    # Aktifkan di Windows
    .\venv\Scripts\Activate

    # Aktifkan di Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Semua Kebutuhan**
    *(Tips pro: Buat file `requirements.txt` dengan mengetik `pip freeze > requirements.txt` di terminal. Ini akan menyimpan semua library yang kamu pakai. Ini adalah praktik standar industri!)*
    ```sh
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi Streamlit**
    ```sh
    streamlit run dashboard.py
    ```
    Aplikasi akan secara otomatis terbuka di browser-mu!

---

### 📁 Struktur Proyek
Berikut adalah tata letak file dan folder dalam repositori ini:

Tentu saja, Mike! Siap, kita revisi.

Struktur yang bagus di README itu krusial, harus sama persis dengan kondisi nyata di folder proyekmu. Ini dia versi yang sudah disesuaikan dengan struktur barumu.

Hapus bagian "Struktur Proyek" yang lama di file README.md kamu, dan ganti dengan semua teks di bawah ini.
Markdown

### 📁 Struktur Proyek

Berikut adalah tata letak file dan folder dalam repositori ini:

DataCleaning-ecommerce/
│
├── 📂 dataset/
│   ├── 📄 inventory_item.csv            # <-- Dataset asli sebelum dibersihkan
│   └── 📄 inventory_item_cleaned_final.csv # <-- Dataset bersih siap pakai untuk dashboard
│
├── 📂 venv/                               # <-- Folder lingkungan virtual Python
│
├── 📄 Project_Prak_SIM.ipynb           # <-- Notebook Jupyter/Colab berisi semua proses analisis & cleaning
├── 📄 dashboard.py                      # <-- Script utama untuk aplikasi dashboard Streamlit
├── 📄 requirements.txt                 # <-- Daftar library yang dibutuhkan untuk menjalankan proyek
└── 📄 README.md                         # <-- File yang sedang Anda baca ini

**Penjelasan Singkat:**
* **`dataset/`**: Folder ini berisi semua file data, baik yang mentah (`inventory_item.csv`) maupun yang sudah bersih (`inventory_item_cleaned_final.csv`).
* **`Project_Prak_SIM.ipynb`**: Ini adalah "buku catatan" atau "ruang kerja" utama kami. Di sinilah semua proses pembersihan data, analisis eksplorasi (EDA), dan visualisasi awal dilakukan.
* **`dashboard.py`**: Script ini mengambil data yang sudah bersih dan mengubahnya menjadi aplikasi web interaktif menggunakan Streamlit.
* **`requirements.txt`**: File ini penting agar orang lain bisa meng-install versi library yang sama persis dengan yang kamu gunakan, cukup dengan satu perintah (`pip install -r requirements.txt`). *(Tips: Buat file ini dengan mengetik `pip freeze > requirements.txt` di terminalmu).*
