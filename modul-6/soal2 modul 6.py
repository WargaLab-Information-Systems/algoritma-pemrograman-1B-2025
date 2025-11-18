def gabung_dan_urutkan(t1, t2):
    gabungan = t1 + t2
    print(f"Hasil gabungan: {gabungan}")
    
    unik = []
    for angka in gabungan:
        if angka not in unik: 
            unik.append(angka)
    print(f"Setelah hapus duplikat: {unik}")
    
    n = len(unik)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unik[j] < unik[j + 1]:
                unik[j], unik[j + 1] = unik[j + 1], unik[j]
    
    print(f"Setelah diurutkan (descending): {unik}")
    

    hasil_akhir = tuple(unik)
    return hasil_akhir


print("=" * 50)
print("PROGRAM MAC ALLISTER - GABUNG DAN URUTKAN TUPLE")
print("=" * 50)

print("\n--- CONTOH DARI SOAL ---")
t1 = (3, 1, 4)
t2 = (1, 5, 9)

print(f"Tuple 1: {t1}")
print(f"Tuple 2: {t2}")
print()

hasil = gabung_dan_urutkan(t1, t2)

print(f"\n>>> HASIL AKHIR: {hasil}")
print(f"Tipe data: {type(hasil)}")

print("\n\n--- CONTOH LAIN ---")
t1 = (7, 2, 9, 2, 5)
t2 = (5, 9, 1, 7, 3)

print(f"Tuple 1: {t1}")
print(f"Tuple 2: {t2}")
print()

hasil2 = gabung_dan_urutkan(t1, t2)

print(f"\n>>> HASIL AKHIR: {hasil2}")

print("\n\n" + "=" * 50)
pilihan = input("Ingin coba dengan tuple sendiri? (y/n): ")

if pilihan.lower() == 'y':
    try:
        print("\nMasukkan angka dipisahkan dengan spasi")
        input1 = input("Tuple 1: ")
        input2 = input("Tuple 2: ")
        t1_user = tuple(map(int, input1.split()))
        t2_user = tuple(map(int, input2.split()))
        
        print(f"\nTuple 1: {t1_user}")
        print(f"Tuple 2: {t2_user}")
        print()
        
        hasil_user = gabung_dan_urutkan(t1_user, t2_user)
        
        print(f"\n>>> HASIL AKHIR: {hasil_user}")
    except:
        print("Error! Pastikan input berupa angka dipisahkan spasi.")
else:
    print("\nProgram selesai!")