def gabungantuple(pertama, kedua):
    gabungan = pertama + kedua
    print("gabuangan angka pertama dan kedua: ",gabungan)

    t = []
    for angka in gabungan:
        ada = False
        for u in t:
            if u == angka:
                ada = True
                break
        if not ada:
            t.append(angka)

    for i in range(len(t) - 1):
        for j in range(i + 1, len(t)):
            if t[i] < t[j]:
                temp = t[i]
                t[i] = t[j]
                t[j] = temp

    return tuple(t)

pertama = (1,5,9,3,0)
print("angka pertama: ",pertama)
kedua = (3,8,6,7,9)
print("angka kedua: ",kedua)
hasil = gabungantuple(pertama, kedua)
print("Hasil akhir:", hasil)