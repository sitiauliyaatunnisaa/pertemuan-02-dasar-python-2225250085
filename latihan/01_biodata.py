"""
Latihan 1 - Biodata Terformat
Nama: [Nama Lengkap]
NIM: [NIM]
Kelas: [Kelas]
"""

TAHUN_SEKARANG = 2026

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan kelas: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))

usia = TAHUN_SEKARANG - tahun_lahir

print("\n=== BIODATA MAHASISWA ===")
print(f"Nama        : {nama}")
print(f"NIM         : {nim}")
print(f"Kelas       : {kelas}")
print(f"Tahun Lahir : {tahun_lahir}")
print(f"Usia        : {usia} tahun")