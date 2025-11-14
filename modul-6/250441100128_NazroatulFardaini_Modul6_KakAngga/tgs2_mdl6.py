def gabung_tuple(t1, t2):
    hasil = []
    
    # Gabungkan keduanya tanpa duplikat
    for i in t1 + t2:
        if i not in hasil:
            hasil.append(i)

    # Urutkan secara menurun (descending)
    for i in range(len(hasil)):
        for j in range(i + 1, len(hasil)):
            if hasil[i] < hasil[j]:
                hasil[i], hasil[j] = hasil[j], hasil[i]

    return tuple(hasil)

# Contoh penggunaan
t1 = (3, 1, 4)
t2 = (1, 5, 9)
print("Hasil gabungan:", gabung_tuple(t1, t2)) 



