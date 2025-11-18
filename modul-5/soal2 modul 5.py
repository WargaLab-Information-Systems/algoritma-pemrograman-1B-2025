def check_anagram (kata1, kata2):
    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if check_anagram (kata1, kata2):
    print("Kedua Kata itu Adalah Anagram")
else:
    print("Kedua Kata itu Bukan Anagram")