print("Program Pemantauan Lampu Taman oleh mas rusdi")

jmlh_baris = int(input("Masukkan total jumlah baris lampu : "))
print("-" * 35)

for i in range(1, jmlh_baris + 1):
    print(f"\n Memeriksa Baris {i}")

    jmlh_lampu = int(input(f"Masukkan jumlah lampu yang ada di baris {i} "))

    for j in range (1, jmlh_lampu + 1):
        pesan_dasar = ""

        if j % 3 == 0:
            pesan_dasar = f"Lampu ke - {j} pada baris {i} Rusak"
        else:
            pesan_dasar =f"Lampu ke - {j} pada baris {i} Nyala"

        pesan_tambah = ""

        if j == jmlh_lampu:
            pesan_tambah = " Periksa sambungan daya utama"

        print(f"{pesan_dasar}{pesan_tambah}")

print("\n" + "=" * 35)
print("Pengecekan selesai")