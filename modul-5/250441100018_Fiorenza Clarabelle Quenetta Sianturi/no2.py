def cek():
    kata1 = input("Masukkan kata pertama: ")
    kata2 = input("Masukkan kata kedua: ")

    kecil1 = ""
    for huruf in kata1:
        if huruf != " ":
            kecil1 = kecil1 + huruf

    kecil2 = ""
    for huruf in kata2:
        if huruf != " ":
            kecil2 = kecil2 + huruf

    panjang1 = 0
    for _ in kecil1:
        panjang1 += 1

    panjang2 = 0
    for _ in kecil2:
        panjang2 += 1

    if panjang1 != panjang2:
        print(f"{kata1} dan {kata2} bukan anagram")
        return

    cocok = True
    for huruf in kecil1:
        beda = False
        baru = ""
        for h in kecil2:
            if h == huruf and not beda:
                beda = True
            else:
                baru = baru + h
        kecil2 = baru
        if not beda:
            cocok = False
            break

    if cocok and kecil2 == "":
        print(f"{kata1} dan {kata2} adalah anagram")
    else:
        print(f"{kata1} dan {kata2} bukan anagram")

cek()
