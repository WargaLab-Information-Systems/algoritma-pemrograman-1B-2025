jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for x in range(1, jumlah_baris + 1):
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{x}: "))
    for y in range(1, jumlah_lampu + 1):
        if y % 3 == 0:
            print(f"Lampu ke-{y} pada baris [{x}] rusak.")
        else:
            print(f"Lampu ke-{y} pada baris [{x}] menyala.")
    if x == jumlah_baris:
        print("Periksa sambungan daya utama.")