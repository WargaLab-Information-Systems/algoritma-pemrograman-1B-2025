t1 = (3, 1, 4)
t2 = (1, 5, 9)

gabung = t1 + t2

unik = []
for angka in gabung:
    if angka not in unik:
        unik.append(angka)

n = len(unik)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if unik[j] < unik[j + 1]:  # jika kiri lebih kecil, tukar
            temp = unik[j]
            unik[j] = unik[j + 1]
            unik[j + 1] = temp

hasil = tuple(unik)

print("Hasil akhir:", hasil)