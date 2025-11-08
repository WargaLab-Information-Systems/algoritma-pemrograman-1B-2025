# Kondisi setiap lampu
jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for baris in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input("Masukkan jumlah lampu pada baris ke-" + str(baris)+ ": "))

    penghitung = 0 # Menghitung kelipatan 3 

    for lampu in range(1, jumlah_lampu +1):
        penghitung += 1

        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
            penghitung = 0
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala")

    if baris == jumlah_baris:
        print("Memeriksa sambungan daya utama")
