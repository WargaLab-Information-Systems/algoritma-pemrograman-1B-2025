jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for nomor_baris in range(1, jumlah_baris + 1):
    
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke- {nomor_baris}: "))
    penghitung = 0  # penghitung kelipatan 3

    for nomor_lampu in range(1, jumlah_lampu + 1):
        penghitung += 1

        if penghitung == 3:
            print(f"Lampu ke- {nomor_lampu} pada baris {nomor_baris} rusak.")
            penghitung = 0  # reset setelah kelipatan 3
        else:
            print(f"Lampu ke- {nomor_lampu} pada baris {nomor_baris} menyala.")

    if nomor_baris == jumlah_baris:
        print("Periksa sambungan daya utama.") 