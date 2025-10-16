# Tarif dasar tol
Mobil_Pribadi =  15000
Truk_Kecil = 25000
Truk_Besar = 40000

# diskon jika bayar pakai e-money
mp = Mobil_Pribadi // 10
tk = Truk_Kecil // 10
tb = Truk_Besar // 10

# diskon jika bayar pakai e-money di jam sepi (23:00 - 05.00)
MP = (Mobil_Pribadi // 100) * 20
TK = (Truk_Kecil // 100) * 20
TB = (Truk_Besar // 100) * 20

# Total yang harus dibayar  setelah diskon e-money
HSDmp = Mobil_Pribadi - mp
HSDtk = Truk_Kecil - tk
HSDtb = Truk_Besar - tb

# Total yang harus dibayar  setelah diskon e-money di jam sepi (23.00- 05.00)
HSDMP = Mobil_Pribadi - MP
HSDTK = Truk_Kecil - TK
HSDTB = Truk_Besar - TB

print("Harga Mobil Pribadi : ", Mobil_Pribadi)
print("Harga Truk Kecil : ", Truk_Kecil)
print("Harga Truk Besar : ", Truk_Besar)
print("Harga Setelah Diskon E-Money mp: ", HSDmp)
print("Harga Setelah Diskon E-Money tk: ", HSDtk)
print("Harga Setelah Diskon E-Money tb: ", HSDtb)
print("Harga Setelah Diskon E-Money di Jam Pagi MP : ", HSDMP)
print("Harga Setelah Diskon E-Money di Jam Pagi TK : ", HSDTK)
print("Harga Setelah Diskon E-Money di Jam Pagi TB : ", HSDTB)