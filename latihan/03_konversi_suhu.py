"""
Latihan 3 - Konversi Suhu
Nama: Siti Auliyaatunnisaa
NIM: 2225250085
Kelas: 3A
"""

KELVIN_OFFSET = 273.15

celsius = float(input("Masukkan suhu Celsius: "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print("\n=== KONVERSI SUHU ===")
print(f"Celsius    : {celsius:.2f} °C")
print(f"Fahrenheit : {fahrenheit:.2f} °F")
print(f"Kelvin     : {kelvin:.2f} K")