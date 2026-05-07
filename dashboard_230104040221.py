import streamlit as st
import pandas as pd
import plotly.express as px
import os
import pickle

st.set_page_config(page_title="Smart Hospital Dashboard", layout="wide")

base_path = os.path.abspath(os.getcwd())
data_total_path = os.path.join(base_path, "output/patient_total")
data_trend_path = os.path.join(base_path, "output/patient_time")

st.title("🏥 Smart Hospital Monitoring System")

st.sidebar.header("Filter")

try:
    # Membaca data Parquet
    df_total = pd.read_parquet(data_total_path)
    df_trend = pd.read_parquet(data_trend_path)
    
    selected_room = st.sidebar.selectbox("Pilih Ruangan", df_total['room'].unique())

    # 1. Tampilan KPI (Total Pasien)
    room_total = df_total[df_total['room'] == selected_room]['total_patients'].values[0]
    st.metric(label=f"Total Pasien Terdata: {selected_room}", value=int(room_total))

    # 2. Grafik Tren Pasien (Line Chart per Jam)
    st.subheader(f"Tren Kepadatan Pasien Per Jam: {selected_room}")
    filtered_trend = df_trend[df_trend['room'] == selected_room].sort_values('hour')
    
    # Menggunakan px.line sesuai perintah "Grafik Tren"
    fig = px.line(filtered_trend, x='hour', y='avg_patients', 
                  markers=True, 
                  labels={'hour': 'Jam Ke-', 'avg_patients': 'Rata-rata Pasien'},
                  title=f"Analisis Tren Waktu di {selected_room}")
    st.plotly_chart(fig, use_container_width=True)

    # 3. Analisis Jam Tertinggi (Output Wajib)
    st.divider()
    peak_row = filtered_trend.loc[filtered_trend['avg_patients'].idxmax()]
    st.info(f"**Analisis Output:** Jam dengan kepadatan pasien tertinggi di ruang **{selected_room}** adalah jam ke-**{int(peak_row['hour'])}** dengan rata-rata **{int(peak_row['avg_patients'])}** pasien.")

    # 4. Prediksi AI (Linear Regression)
    st.subheader("🔮 Prediksi Jumlah Pasien (AI)")
    hour_input = st.slider("Pilih Jam untuk Prediksi (0-23)", 0, 23, 12)
    
    if os.path.exists('model_lr.pkl'):
        with open('model_lr.pkl', 'rb') as f:
            model = pickle.load(f)
        prediction = model.predict([[hour_input]])
        st.success(f"Hasil Prediksi AI pada jam {hour_input}:00 adalah {int(prediction[0])} pasien.")

except Exception as e:
    st.error(f"Gagal memproses data. Silakan jalankan file 'main_uts' terlebih dahulu. Detail: {e}")