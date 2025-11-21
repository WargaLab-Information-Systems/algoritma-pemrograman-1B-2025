baris_lampu = (input("masukkan jumlah baris lampu:"))
while not all(c in "0123456789" for c in baris_lampu):
    print("masukkan angka aja")
    baris_lampu = input("masukkan jumlah baris lampu:")
baris_lampu = int(baris_lampu)

for baris in range(1, baris_lampu + 1):
    jumlah_lampu = (input(f"masukkan jumlah lampu pada baris {baris}:"))
    while not all(c in "0123456789" for c in jumlah_lampu):
        print("masukkan angka aja")
        jumlah_lampu = input("masukkan jumlah lampu pada baris: ")
    jumlah_lampu = int(jumlah_lampu)

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print(f"lampu ke-{lampu} pada baris {baris} rusak.")
        else:
            print(f"lampu ke-{lampu} pada baris {baris} menyala.")

#jika baris terakhir, tambahkan pesan khusus
if baris == baris_lampu:
    print("periksa sambungan daya utama")