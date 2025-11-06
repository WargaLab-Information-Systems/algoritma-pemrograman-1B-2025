n = int(input("Masukkan jumlah baris lampu: "))
lampu_counter = 1
for baris in range(1, n + 1):
    m = int(input(f"Masukkan jumlah lampu di baris {baris}: "))
    for lampu in range(1, m + 1):
        if lampu_counter % 3 == 0:
            print(f"Lampu ke-{lampu_counter} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu_counter} pada baris {baris} menyala.")
        lampu_counter += 1
    if baris == n:
        print("Periksa sambungan daya utama.")
