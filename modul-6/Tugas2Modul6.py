def gabung_urut_tuple(t1, t2):  #fungsi menerima 2 tuple
    gabungan = t1 + t2

    unik = [] #list kosong untuk menampung angka tnpa duplikat
    for angka in gabungan:
        sudah_ada = False   #tanda bahwa angka tsb blm ada di list unik
        for u in unik:      #cek satu persatu isi list unik 
            if u == angka:
                sudah_ada = True    #kalo angka sdh ada hentikan
                break
        if not sudah_ada:       #jika blm ada trs tambahkan ke list unik
            unik.append(angka)

    for i in range(len(unik) - 1): #ngurutin dari terbesar ke terkecil
        for j in range(i + 1, len(unik)):   #melakukan perbandingan angka ke-i dgn angka-j
            if unik[i] < unik[j]:
                # Tukar posisi
                tempat = unik[i]
                unik[i] = unik[j]
                unik[j] = tempat

    return tuple(unik)      #klo udh urut&tdk duplikat dijadikan tuple lg

t1 = (16, 3, 6) #tuple
t2 = (1, 5, 9)

hasil_akhir = gabung_urut_tuple(t1, t2)     #manggil fungsi gabunguruttuple & nyimpan hasil di hasilakhir

print(f"Tuple pertama: {t1}")
print(f"Tuple kedua: {t2}")
print(f"Hasil gabungan (unik, urut menurun): {hasil_akhir}")



