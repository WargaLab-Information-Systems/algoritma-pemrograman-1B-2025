def cek_anagram(kata1, kata2):
    
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

hasil = cek_anagram(kata1, kata2)

print(f"Kata pertama : {kata1}")
print(f"Kata kedua   : {kata2}")
print("Apakah anagram?", hasil)

if hasil:
    print("Kedua kata merupakan anagram.")
else:
    print("Kedua kata bukan anagram.")