import math  # Mengimpor library math yang menyediakan operasi matematika seperti pi

# Lambda anonymous function untuk menghitung luas lingkaran
# menerima parameter r dan mengembalikan hasil perhitungan luas lingkaran dengan rumus pi * r^2
luas = lambda r: math.pi * r ** 2

# Mengambil input dari user
# jari-jari (radius) lingkaran dengan tipe data float agar bisa digunakan dalam perhitungan
radius = float(input("Masukkan jari-jari lingkaran: "))

# Memanggil fungsi lambda 'luas' dengan memasukkan nilai radius, kemudian menyimpan hasilnya di variabel Luas
Luas = luas(radius)

# Menampilkan hasil luas lingkaran ke layar dengan menggunakan formatted string (f-string)
print(f"Luas lingkaran dengan jari-jari {radius} adalah {Luas}")
