def cek_anagram(kata1, kata2):
    kata1 = sorted(kata1.lower())
    kata2 = sorted(kata2.lower())
    return kata1 == kata2

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if kata1 == kata2:
    print ("kedua kata tersbut bukan anagram")
elif cek_anagram(kata1, kata2):
    print("Kedua kata tersebut merupakan anagram.")
else:
    print("Kedua kata tersebut bukan anagram.")
