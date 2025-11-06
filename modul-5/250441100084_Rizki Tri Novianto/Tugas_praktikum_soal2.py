def cek_anagram(kata1, kata2):
    # merubah huruf agar tidak ada kapital
    kata1 = kata1.lower()
    kata2 = kata2.lower()
    
    # Bandingkan hasil pengurutan huruf
    return sorted(kata1) == sorted(kata2)

# Input dari pengguna

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("Kedua kata merupakan anagram ")
else:
    print("Kedua kata bukan anagram ")

    
cek_anagram(kata1, kata2)