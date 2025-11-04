def anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    if sorted(kata1) == sorted(kata2): 
        return True

kat = input("Masukkan kata pertama: ")
kat1 = input("Masukkan kata kedua: ")
kalimat = anagram(kat, kat1)
if kalimat:
    print("Kedua kata tersebut adalah anagram.")
else:
    print("Kedua kata tersebut bukan anagram.")