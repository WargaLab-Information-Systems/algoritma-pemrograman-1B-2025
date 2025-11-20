def gabungantuple(t1, t2):
    gabungan = t1 + t2

    # Hapus duplikat sambil mempertahankan urutan asli
    u = []
    for angka in gabungan:
        sudah_ada = False
        for k in u:
            if k == angka:
                sudah_ada = True
                break
        if not sudah_ada:
            u.append(angka)

    # untuk mengurutkan dari besar ke kecil (descending)
    for i in range(len(u)):
        for j in range(i + 1, len(u)):
            if u[i] < u[j]:
                u[i], u[j] = u[j], u[i]
    return tuple(u)


t1 = (13 ,2 ,5)
t2 = (1, 5, 9)
hasil = gabungantuple(t1, t2)
print("Hasil akhir:", hasil)

buah = ["apel", "jeruk", "mangga", "pisang", "kiwi"]
buah [1] =("nanas")
print(buah)