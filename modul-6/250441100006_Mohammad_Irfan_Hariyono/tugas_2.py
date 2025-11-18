def gabung_urut_tuple(t1, t2):
    gabungan = t1 + t2

    unik = []
    for angka in gabungan:
        sudah_ada = False
        for u in unik:
            if u == angka:
                sudah_ada = True
                break
        if not sudah_ada:
            unik.append(angka)

    for i in range(len(unik) - 1):
        for j in range(i + 1, len(unik)):
            if unik[i] < unik[j]:
                temp = unik[i]
                unik[i] = unik[j]
                unik[j] = temp

    return tuple(unik)

t1 = (3, 1, 4)
t2 = (1, 5, 9)

hasil_akhir = gabung_urut_tuple(t1, t2)

print(f"Tuple pertama: {t1}")
print(f"Tuple kedua: {t2}")
print(f"Hasil gabungan (unik, urut menurun): {hasil_akhir}")

print("-" * 20)

t3 = (9, 0, 5, 1, 10, 2, 0)
t4 = (8, 5, 2, 3, 7)
hasil_akhir_2 = gabung_urut_tuple(t3, t4)
print(f"Tuple ketiga: {t3}")
print(f"Tuple keempat: {t4}")
print(f"Hasil gabungan (unik, urut menurun): {hasil_akhir_2}")

t5 =(12,10,11)
t6 =(14,11,13)
hasil_akhir_3 =gabung_urut_tuple(t5, t6)
print(f"Tuple ketiga: {t5}")
print(f"Tuple keempat: {t6}")
print(f"Hasil gabungan (unik, urut menurun): {hasil_akhir_3}")