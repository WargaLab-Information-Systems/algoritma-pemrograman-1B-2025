# jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

# for y in range(1, jumlah_baris + 1):
#     jumlah_lampu = int(input(f"Masukkan jumlah lampu di baris {y}: "))
    
#     for x in range(1, jumlah_lampu + 1):
#         if x % 3 == 0:
#             print(f"Lampu ke-{x} pada baris {y} rusak.")
#         else:
#             print(f"Lampu ke-{x} pada baris {y} menyala.")
           
#     if y == jumlah_baris:
#         print("Periksa sambungan daya utama.")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end="t/")
    print()