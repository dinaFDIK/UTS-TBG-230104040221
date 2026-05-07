import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from datetime import datetime, timedelta
import random
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("SmartHospitalMonitoring") \
    .config("spark.sql.parquet.v2.enabled", "false") \
    .getOrCreate()

base_path = os.path.abspath(os.getcwd())
output_path = os.path.join(base_path, "output")

# 1. Simulasi Data Pasien (Data dibuat per jam)
data = []
rooms = ["ICU", "Emergency", "Pharmacy"]
start_time = datetime.now().replace(minute=0, second=0, microsecond=0)

for i in range(24): # Simulasi data untuk 24 jam
    timestamp = start_time + timedelta(hours=i)
    for room in rooms:
        patient_count = random.randint(10, 100)
        data.append((timestamp, room, patient_count))

columns = ["timestamp", "room", "patient_count"]
df = spark.createDataFrame(data, schema=columns)

# 2. Transformasi Data
# Agregasi rata-rata per jam
df_hourly = df.withColumn("hour", F.hour("timestamp")) \
              .groupBy("hour", "room") \
              .agg(F.avg("patient_count").alias("avg_patients")) \
              .orderBy("hour")

# Total akumulasi pasien per ruangan
total_per_room = df.groupBy("room").agg(F.sum("patient_count").alias("total_patients"))

# 3. Simpan ke Parquet (Absolute Path & Overwrite)
total_per_room.write.mode("overwrite").parquet(os.path.join(output_path, "patient_total"))
df_hourly.write.mode("overwrite").parquet(os.path.join(output_path, "patient_time"))

print(f"--- Data Parquet Berhasil Disimpan di: {output_path} ---")

# 4. Machine Learning (Linear Regression)
pandas_df = df_hourly.toPandas()
X = pandas_df[['hour']]
y = pandas_df['avg_patients']

model = LinearRegression()
model.fit(X, y)

with open('model_lr.pkl', 'wb') as f:
    pickle.dump(model, f)

print("--- Model ML Berhasil Dilatih ---")
spark.stop()