#ada bola dalam sebuah kotak dan bermacam macam warnanya
#warna dan jumlah bola yang diketahui yaitu: bola merah = 8, bola biru = 6,
#dan bola warna acak = 3


import math #python tidak bisa mengetahui apa itu match, factorial atau math, comb
#jadi kita menggunakan def itu sebagai didefinisikan dari combbinasi agar terbaca

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

#Total bola yang di ambil 
total_bola = 8 + 6
diambil = 3


kombinasi = comb(total_bola, diambil)
print("jumlah kemungkianan bola yang terambil : ", kombinasi)