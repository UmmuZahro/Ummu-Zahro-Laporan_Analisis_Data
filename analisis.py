import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Baca dataset
data = pd.read_csv('nilai_siswa.csv')

# 2. Tampilkan info dataset
print("=== INFO DATASET ===")
print(data.info())

# 3. Tampilkan 5 data pertama
print("\n=== 5 DATA PERTAMA ===")
print(data.head())

# 4. Statistik deskriptif
print("\n=== STATISTIK DESKRIPTIF ===")
print(data.describe())

# 5. Hitung ukuran statistik dasar
print("\n=== PERHITUNGAN STATISTIK ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# 6. Nilai per mata pelajaran
print("\n=== NILAI PER MAPEL ===")
for mapel in data['Mapel'].unique():
    print(f"\n{mapel}:")
    print(data[data['Mapel'] == mapel])

# 7. Nilai maksimum & minimum per mapel
print("\n=== MAX & MIN PER MAPEL ===")
print(data.groupby('Mapel')['Nilai'].agg(['max', 'min']))

# 8. Grafik rata-rata nilai per mapel
rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata').
plt.show()

# 9. Boxplot sebaran nilai
sns.boxplot(x='Mapel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()