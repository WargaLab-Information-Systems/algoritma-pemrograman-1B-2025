# Sederhanakan input jumlah baris dengan validasi
while True:
    baris_str = input("Masukkan jumlah baris lampu: ")
    if baris_str.isdigit() and int(baris_str) > 0:
        jumlah_baris = int(baris_str)
        break
    print("Input tidak valid. Masukkan angka positif saja.")

# Looping utama untuk setiap baris
for y in range(1, jumlah_baris + 1):
    # Meminta jumlah lampu di baris ke-y. Tidak perlu int() karena input() sudah int
    jumlah_lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{y}: "))

    # Looping untuk setiap lampu di baris tersebut
    for x in range(1, jumlah_lampu + 1):
        # Cek kelipatan 3 (Lampu Rusak)
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak.")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala.")

    # Cek apakah ini baris terakhir
    if y == jumlah_baris:
        print("Periksa sambungan daya utama.")

