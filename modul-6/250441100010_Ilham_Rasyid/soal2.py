t1 = (3, 1, 4)
t2 = (1, 5, 9)

gabung = t1 + t2

unik = []
for angka in gabung:
    if angka not in unik:
        unik.append(angka)

n = len(unik)
for i in range(n):
    for j in range(0, n - 1):
        if unik[j] < unik[j + 1]:   
            unik[j], unik[j + 1] = unik[j + 1], unik[j]

hasil = tuple(unik)

print(hasil)