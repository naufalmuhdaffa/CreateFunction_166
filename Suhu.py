def konversiSuhu(value, unit):  
    # Mendefinisikan fungsi konversiSuhu yang menerima dua parameter:
    # 'value' untuk nilai suhu, dan 'unit' untuk satuan suhu ('C' atau 'F')
    
    if unit == 'F':  
        # Jika yang diminta adalah 'F', maka lakukan konversi dari Celsius ke Fahrenheit
        return (value * 9/5) + 32  # Rumus konversi dari Celsius ke Fahrenheit
        
    elif unit == 'C':  
        # Jika yang diminta adalah 'C', maka lakukan konversi dari Fahrenheit ke Celsius
        return (value - 32) * 5/9  # Rumus konversi dari Fahrenheit ke Celsius
        
    else:  
        # Jika unit tidak valid, kembalikan pesan error
        return "Unit tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."

# Mengambil input suhu dari user dalam bentuk float
suhu = float(input("Masukkan nilai suhu: "))

# Mengambil input unit suhu ('C' atau 'F') dari user
# kemudian mengubahnya menjadi huruf besar agar bisa dibandingkan tanpa case-sensitivity
unit = input("Masukkan unit suhu ('C' untuk konversi Fahrenheit ke Celsius, 'F' untuk konversi Celsius ke Fahrenheit): ").upper()

# Memanggil fungsi konversiSuhu dengan nilai suhu dan unit yang diberikan oleh user
konversi = konversiSuhu(suhu, unit)

# Menampilkan hasil konversi suhu ke layar
print(f"Hasil konversi: {konversi}")
