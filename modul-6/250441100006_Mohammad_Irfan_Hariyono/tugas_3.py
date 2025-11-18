def cek_input_numerik(teks_input):
    if len(teks_input) == 0:
        return False
        
    for huruf in teks_input:
        if huruf not in "0123456789":
            return False
            
    return True

def sisip_nilai(data_list):
    print("\n1. Tambah Angka")
    teks_input = input("Masukkan angka (positif) yang akan ditambah: ")
    
    if cek_input_numerik(teks_input):
        nilai = int(teks_input)
        data_list.append(nilai)
        print(f"Angka {nilai} berhasil ditambahkan.")
    else:
        print("Tidak valid, Harap masukkan angka positif.")

def cetak_list(data_list):
    print("\n2. Tampilkan Deretan Angka")
    
    if not data_list: 
        print("Deretan masih kosong.")
        return False
    else:
        print(f"Deretan Anda saat ini: {data_list}")
        return True

def ganti_nilai(data_list):
    print("\n3. Ubah Angka")
    if not cetak_list(data_list): 
        return

    teks_indeks = input("Masukkan nomor urut (indeks) yang akan diubah (dimulai dari 0): ")
    
    if not cek_input_numerik(teks_indeks):
        print("Input indeks tidak valid! Harus berupa angka.")
        return
        
    posisi = int(teks_indeks)
    
    total_data = len(data_list)
    if posisi < 0 or posisi >= total_data:
        print(f"Indeks {posisi} di luar jangkauan! Indeks yang valid: 0 sampai {total_data - 1}")
        return

    teks_nilai_baru = input(f"Masukkan angka baru untuk menggantikan {data_list[posisi]}: ")
    
    if not cek_input_numerik(teks_nilai_baru):
        print("Input nilai baru tidak valid! Harus angka positif.")
        return
        
    angka_lama = data_list[posisi]
    angka_baru = int(teks_nilai_baru)
    
    data_list[posisi] = angka_baru 
    
    print(f"Sukses! Angka {angka_lama} di indeks {posisi} telah diubah menjadi {angka_baru}.")

def buang_nilai(data_list):
    print("\n4. Hapus Angka")
    if not cetak_list(data_list):
        return

    teks_indeks = input("Masukkan nomor urut (indeks) yang akan dihapus (dimulai dari 0): ")
    
    if not cek_input_numerik(teks_indeks):
        print("Input indeks tidak valid! Harus berupa angka.")
        return
        
    posisi = int(teks_indeks)

    total_data = len(data_list)
    if posisi < 0 or posisi >= total_data:
        print(f"Indeks {posisi} di luar jangkauan! Indeks yang valid: 0 sampai {total_data - 1}")
        return
        
    nilai_dihapus = data_list[posisi] 
    
    del data_list[posisi]
    
    print(f"Sukses! Angka {nilai_dihapus} di indeks {posisi} telah dihapus.")

def periksa_keseimbangan(data_list):
    print("\n5. Cek Pembagian Jumlah Sama")
    cetak_list(data_list)
    
    total_data = len(data_list)
    
    if total_data == 0:
        print("Deretan kosong. Tidak bisa dicek.")
        print("Hasil: False")
        return

    if total_data % 2 != 0:
        print("Jumlah angka ganjil, tidak bisa dibagi dua bagian sama rata.")
        print("Hasil: False")
        return
        
    titik_tengah = total_data // 2
    
    slice_kiri = data_list[:titik_tengah]
    slice_kanan = data_list[titik_tengah:]
    
    tuple_kiri = tuple(slice_kiri)
    tuple_kanan = tuple(slice_kanan)
    
    total_kiri = sum(tuple_kiri)
    total_kanan = sum(tuple_kanan)
    
    print(f"Bagian Kiri: {tuple_kiri}")
    print(f"Bagian Kanan: {tuple_kanan}")
    print(f"Jumlah Kiri: {total_kiri}")
    print(f"Jumlah Kanan: {total_kanan}")
    
    if total_kiri == total_kanan:
        print("Jumlah kedua bagian SAMA.")
        print("Hasil: True")
    else:
        print("Jumlah kedua bagian BERBEDA.")
        print("Hasil: False")

def jalankan_program():
    kumpulan_angka = [] 
    
    while True:
        print("\nProgram Pengecekan Angka")
        print("1. Tambah Angka (Create)")
        print("2. Tampilkan Angka (Read)")
        print("3. Ubah Angka (Update)")
        print("4. Hapus Angka (Delete)")
        print("5. Cek Pembagian Jumlah Sama")
        print("6. Keluar")
        
        menu = input("Silakan pilih menu (1-6): ")
        
        if menu == '1':
            sisip_nilai(kumpulan_angka) 
            
        elif menu == '2':
            cetak_list(kumpulan_angka)
            
        elif menu == '3':
            ganti_nilai(kumpulan_angka)
            
        elif menu == '4':
            buang_nilai(kumpulan_angka)
            
        elif menu == '5':
            periksa_keseimbangan(kumpulan_angka)
            
        elif menu == '6':
            print("\nTerima kasih! Program ditutup.")
            break
        else:
            print("\nPilihan tidak valid. Harap masukkan angka 1 sampai 6.")

if __name__ == "__main__":
    jalankan_program()