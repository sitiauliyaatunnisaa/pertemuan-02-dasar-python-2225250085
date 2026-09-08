"""
Latihan 4 - Nilai Akhir
Nama: Siti Auliyaatunnisaa
NIM: 2225250085
Kelas: 3A
"""

nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (
    0.20 * nilai_tugas
    + 0.30 * nilai_uts
    + 0.50 * nilai_uas
)

print("\n=== NILAI AKHIR MAHASISWA ===")
print(f"Nama        : {nama}")
print(f"Nilai Tugas : {nilai_tugas:.2f}")
print(f"Nilai UTS   : {nilai_uts:.2f}")
print(f"Nilai UAS   : {nilai_uas:.2f}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")