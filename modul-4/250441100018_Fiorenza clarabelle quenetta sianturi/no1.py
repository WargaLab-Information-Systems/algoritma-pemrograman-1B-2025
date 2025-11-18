l = int(input("Masukkan jumlah baris lampu: "))

lampu = 1

for baris in range(1, l + 1):
    b = int(input(f"Masukkan jumlah lampu di baris {baris}: "))
    
    for _ in range(b):
        if lampu % 3 == 0:
            print(f"Lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"Lampu ke-{lampu} pada baris {baris} menyala.")
        lampu += 1
    print()
    
    if baris == l:
        print("Periksa sambungan daya utama.")
