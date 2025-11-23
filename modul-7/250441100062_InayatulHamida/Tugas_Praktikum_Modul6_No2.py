def gabungkan_tuple(t1, t2):
    gabungan = t1 + t2
    
    tanpa_duplikat = []
    for angka in gabungan:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)

    hasil_terurut = []
    while tanpa_duplikat:
        max_angka = tanpa_duplikat[0]
        for angka in tanpa_duplikat:
            if angka > max_angka:
                max_angka = angka
        
        hasil_terurut.append(max_angka)
        tanpa_duplikat.remove(max_angka)

    return tuple(hasil_terurut)

t1 = (3, 1, 4)
t2 = (1, 5, 9)
hasil = gabungkan_tuple(t1, t2)

print(hasil) 