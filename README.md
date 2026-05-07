# 🏥 Smart Hospital Monitoring System

## 📊 Big Data Pipeline using PySpark, Parquet, Machine Learning & Streamlit

---

## 📌 Deskripsi Project

**Smart Hospital Monitoring System** merupakan project Ujian Tengah Semester (UTS) mata kuliah **Teknologi Big Data** yang bertujuan membangun pipeline Big Data sederhana untuk memonitor jumlah pasien pada beberapa ruangan rumah sakit menggunakan data simulasi sensor IoT.

Project ini mengimplementasikan:
- Data generation menggunakan Python
- Data processing menggunakan PySpark
- Penyimpanan data ke format Parquet
- Prediksi jumlah pasien menggunakan Machine Learning
- Dashboard interaktif menggunakan Streamlit & Plotly

Pipeline sistem:

```text
Patient Sensor Data
        ↓
Spark Processing
        ↓
Parquet Storage
        ↓
AI Prediction
        ↓
Streamlit Dashboard
```

---

## 🎯 Tujuan Project

- Memahami implementasi Big Data Pipeline
- Menggunakan PySpark untuk transformasi data
- Mengelola penyimpanan data menggunakan format Parquet
- Mengimplementasikan Machine Learning sederhana
- Membuat dashboard visualisasi data interaktif menggunakan Streamlit

---

## 🛠️ Teknologi yang Digunakan

- Python
- Apache Spark (PySpark)
- Streamlit
- Plotly
- Scikit-Learn
- Parquet File Format
- Linux / WSL

---

## 📂 Struktur Project

```text
uts-tbg-230104040221/
│
├── main_uts_230104040221.py
├── dashboard_230104040221.py
│
├── output/
│   ├── patient_total/
│   ├── patient_time/
│   └── ml_data/
│
├── screenshots/
│   ├── parquet-success.png
│   └── dashboard.png
│
└── README.md
```

---

## 🧪 Studi Kasus

Rumah sakit modern memiliki ribuan sensor IoT untuk memantau jumlah pasien pada beberapa ruangan layanan. Sistem Big Data digunakan untuk menganalisis kepadatan pasien dan memprediksi jumlah pasien pada jam tertentu.

### Ruangan yang digunakan:
- ICU
- Emergency
- Pharmacy

### Data Simulasi:
- Durasi: 120 menit
- Jumlah pasien random: 5–80 pasien

### Field Data:
- `timestamp`
- `room`
- `patient_count`

---

## ⚙️ Fitur Implementasi

### 1️⃣ Generate Dummy Data
Program menghasilkan data simulasi sensor pasien secara otomatis menggunakan Python.

### 2️⃣ Spark Transformation
Transformasi data menggunakan PySpark:
- Total pasien per ruangan
- Tren pasien setiap 15 menit
- Dataset AI berbasis jam

### 3️⃣ Penyimpanan Parquet
Hasil transformasi disimpan ke format Parquet pada folder:

```text
output/patient_total
output/patient_time
output/ml_data
```

Menggunakan:
- mode overwrite
- absolute path

### 4️⃣ Dashboard Streamlit
Dashboard memiliki fitur:
- Sidebar filter ruangan
- KPI total pasien
- Grafik tren pasien
- Prediksi jumlah pasien berdasarkan jam

### 5️⃣ Machine Learning
Model AI menggunakan:
- Linear Regression

Input:
- `hour`

Output:
- `patient_count`

Digunakan untuk memprediksi jumlah pasien berdasarkan jam tertentu.

---

## ▶️ Cara Menjalankan Project

### 1. Jalankan Spark Engine

```bash
python3 main_uts_230104040221.py
```

### 2. Jalankan Dashboard Streamlit

```bash
streamlit run dashboard_230104040221.py
```

---

## 🧪 Hasil Pengujian

### ✅ Screenshot Terminal Parquet Berhasil

```text
./screenshots/parquet-success.png
```

![Parquet Success](./screenshots/parquet-success.png)

---

### ✅ Screenshot Dashboard Streamlit

```text
./screenshots/dashboard.png
```

![Dashboard](./screenshots/dashboard.png)

---

## 📈 Analisis Hasil

Berdasarkan hasil visualisasi dashboard dan prediksi Machine Learning, jumlah pasien tertinggi terjadi pada jam-jam sibuk rumah sakit, terutama pada ruang Emergency dan ICU.

Model Linear Regression berhasil memberikan prediksi tren jumlah pasien berdasarkan data historis yang dihasilkan dari sensor IoT simulasi.

---

## ✅ Checklist Validasi

- [✅] Spark berhasil dijalankan
- [✅] File parquet berhasil dibuat
- [✅] Dashboard Streamlit berjalan
- [✅] Grafik Plotly tampil
- [✅] Prediksi AI berjalan
- [✅] Filter sidebar berfungsi

---

## 👩‍🎓 Identitas Mahasiswa

- **Nama** : Dina Muzaina Aqillah
- **NIM** : 230104040221
- **Kelas** : TI23A
- **Mata Kuliah** : Teknologi Big Data
- **Dosen Pengampu** : Muhayat, M.IT

---

## ✍️ Catatan

Project ini dibuat sebagai implementasi Ujian Tengah Semester (UTS) mata kuliah Teknologi Big Data dengan tema implementasi Big Data Pipeline menggunakan PySpark, Parquet, Machine Learning, dan Streamlit Dashboard.