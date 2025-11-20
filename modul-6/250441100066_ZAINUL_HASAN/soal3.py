# angka = []

# while True:
#     print("PILIH MENU")
#     print("1. Tambah angka")
#     print("2. Tampilkan angka")
#     print("3. Ubah angka")
#     print("4. Hapus angka")
#     print("5. Cek pembagian sama")
#     print("6. Keluar")

#     pilih = input("Pilih menu: ")

#     if pilih == "1":
#         angka.append(int(input("Masukkan angka: ")))

#     elif pilih == "2":
#         print("Daftar angka:", angka)

#     elif pilih == "3":
#         i = int(input("Indeks yang ingin diubah: "))
#         if 0 <= i < len(angka):
#             angka[i] = int(input("Masukkan nilai baru: "))
#         else:
#             print("Indeks tidak valid!")

#     elif pilih == "4":
#         i = int(input("Indeks yang ingin dihapus: "))
#         if 0 <= i < len(angka):
#             angka.pop(i) 
#         else:
#             print("Indeks tidak valid!")

#     elif pilih == "5":
#         if len(angka) % 2 == 0 and len(angka) > 0:
#             tengah = len(angka)//2
#             kiri, kanan = angka[:tengah], angka[tengah:]
#             print("Bagian 1:", kiri)
#             print("Bagian 2:", kanan)
#             print("Hasil:", sum(kiri) == sum(kanan))
#         else:
#             print("Jumlah elemen harus genap dan tidak kosong!")
  
#     elif pilih == "6":
#         print("Program selesai.")
#         break

#     else:
#         print("Pilihan tidak valid!")




outfit = ('baju', 'celana', 'rok')
for i in outfit :
    for j in outfit:
        for k in outfit:
            print('kombinasi outfit hari ini', i, j, k)
