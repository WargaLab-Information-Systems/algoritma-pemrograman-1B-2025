jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

baris = 1
while baris <= jumlah_baris:
    jumlah_lampu = int(input(f"Masukkan jumlah lampu di baris {baris}: "))
    for nomor_lampu in range(1, jumlah_lampu + 1):
        if nomor_lampu % 3 == 0:
            print(f"Lampu ke-{nomor_lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{nomor_lampu} pada baris {baris} menyala.")
    if baris == jumlah_baris:
        print("Periksa sambungan daya utama.")
    print() 
    baris += 1


