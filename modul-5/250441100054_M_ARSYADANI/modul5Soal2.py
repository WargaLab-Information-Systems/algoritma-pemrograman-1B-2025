def IsAnagram(kata1, kata2):
    kata1 =sorted(kata1)
    kata2 =sorted(kata2)

    return kata1 == kata2

#main
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")


if kata1 == kata2:
     print(f"'{kata1}'dan'{kata2}'adalah bukan kata anagram")
else:
    print(f"'{kata1}'dan'{kata2}'adalah  kata anagram")