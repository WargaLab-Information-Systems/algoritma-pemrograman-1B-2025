# Lampu Taman Kota
print("=== Program Lampu Mas Narji ===")
baris = int(input("Masukkan jumlah baris lampu: "))

for i in range(1, baris + 1):
    jumlah_lampu = int(input(f"\nMasukkan jumlah lampu pada baris ke-{i}: "))
    
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"Baris Lampu ke-{i} pada Lampu ke-{j} rusak.")
        else:
            print(f"Baris Lampu ke-{i} pada Lampu ke-{j} menyala.")
    if i == baris:
        print("Periksa sambungan daya utama.\n")
    

