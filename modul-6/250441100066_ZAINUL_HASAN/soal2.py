
t1 = (3, 1, 4)
t2 = (1, 5, 9)

gabung = t1 + t2
hasil = []
for x in gabung:
    if x not in hasil: 
        hasil.append(x)

for i in range(len(hasil)):
    for j in range(i + 1, len(hasil)):
        if hasil[i] < hasil[j]:
            hasil[i], hasil[j] = hasil[j], hasil[i]

print(hasil)