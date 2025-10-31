# Program untuk menampilkan kondisi lampu di taman kota

# Meminta jumlah baris lampu
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# Perulangan untuk setiap baris
for baris in range(1, jumlah_baris + 1):
    # Meminta jumlah lampu di baris tersebut
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris {baris}: "))

    # Perulangan untuk setiap lampu di baris
    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
    
    # Jika baris terakhir, tampilkan peringatan tambahan
    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.")
