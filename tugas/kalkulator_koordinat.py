"""
Tugas Utama - Kalkulator Koordinat
Nama: Siti Auliyaatunnisaa
NIM: 2225250085
Kelas: 3A

Program untuk menghitung jarak antara dua titik
dan titik tengah dari dua titik pada bidang koordinat.
"""

x1 = float(input("Masukkan koordinat x titik A: "))
y1 = float(input("Masukkan koordinat y titik A: "))

x2 = float(input("Masukkan koordinat x titik B: "))
y2 = float(input("Masukkan koordinat y titik B: "))

# Menghitung selisih koordinat x dan y
dx = x2 - x1
dy = y2 - y1

# Menghitung jarak antara titik A dan titik B
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Menghitung titik tengah antara titik A dan titik B
titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

print("\n=== KALKULATOR KOORDINAT ===")
print(f"Titik A        : ({x1:.2f}, {y1:.2f})")
print(f"Titik B        : ({x2:.2f}, {y2:.2f})")
print(f"dx             : {dx:.2f}")
print(f"dy             : {dy:.2f}")
print(f"Jarak          : {jarak:.2f}")
print(f"Titik Tengah   : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")