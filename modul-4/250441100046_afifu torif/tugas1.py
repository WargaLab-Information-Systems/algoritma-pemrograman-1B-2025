baris = int(input("Masukkan jumlah baris lampu: "))
for i in range(1, baris + 1):
    lampu = int(input(f"Masukkan jumlah lampu pada baris ke-{i}: "))
    for j in range(1, lampu + 1):
        if j % 3 == 0:
            print(f"Lampu ke-{j} pada baris {i} rusak.")
        else:
            print(f"Lampu ke-{j} pada baris {i} menyala.")
    if i == baris:
        print("Periksa sambungan daya utama.")