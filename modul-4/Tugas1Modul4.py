while True:
    jumlah_baris = input("Masukkan jumlah baris lampu: ")
    if jumlah_baris.isdigit():
        jumlah_baris = int(jumlah_baris)
        break
    else:
        print("Input tidak valid! Masukkan angka, bukan huruf.")

for y in range(1, jumlah_baris + 1):
    while True:
        jumlah_lampu = input(f"Masukkan jumlah lampu pada baris ke: ")
        if jumlah_lampu.isdigit():
            jumlah_lampu = int(jumlah_lampu)
            break
        else:
            print("Input tidak valid! Masukkan angka, bukan huruf.")

    for x in range(1, jumlah_lampu + 1):
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")

    if y == jumlah_baris:
        print("Periksa sambungan daya utama.")
















