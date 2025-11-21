satu1 = (12, 13, 10)
dua2 = (7, 5, 4)

mix = satu1 + dua2

tanpa_kembar = []
for angka in mix:
    if angka not in tanpa_kembar:
        tanpa_kembar.append(angka)

for i in range(len(tanpa_kembar)):
    for j in range(i + 1, len(tanpa_kembar)):
        if tanpa_kembar[i] < tanpa_kembar[j]:
            smntara = tanpa_kembar[i]
            tanpa_kembar[i] = tanpa_kembar[j]
            tanpa_kembar[j] = smntara

hasil = tuple(tanpa_kembar)
print("Hasil akhir nya yaitu: ", hasil)

