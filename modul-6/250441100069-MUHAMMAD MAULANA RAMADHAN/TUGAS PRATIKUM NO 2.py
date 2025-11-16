print("=== PROGRAM GABUNGAN TUPLE MAC ALLISTER ===")


def validasi(teks):
    ada_angka = False
    for karakter in teks:
        if karakter == " ":
            continue
        elif karakter >= "0" and karakter <= "9":
            ada_angka = True
        else:
            return False
    return ada_angka

def string_ke_tuple(teks):
    hasil = ()
    angka = ""

    for karakter in teks + " ":
        if karakter == " " and angka != "":
            hasil = hasil + (int(angka),)
            angka = ""
        elif karakter != " ":
            angka += karakter

    return hasil

def hapus_duplikat(tup):
    hasil = ()
    for x in tup:
        ada = False
        for y in hasil:
            if x == y:
                ada = True
                break
        if not ada:
            hasil = hasil + (x,)
    return hasil

def urut_desc(tup):
    hasil = ()
    data = tup

    while data != ():
        maks = data[0]
        sisa = ()
        pertama = True

        for elemen in data:
            if pertama:
                pertama = False
                continue
            if elemen > maks:
                sisa += (maks,)
                maks = elemen
            else:
                sisa += (elemen,)

        hasil += (maks,)
        data = sisa

    return hasil

while True:
    teks1 = input("\nMasukkan angka tuple pertama (pisahkan dengan spasi): ")
    if validasi(teks1):
        break
    print("Input tidak valid!")

while True:
    teks2 = input("\nMasukkan angka tuple kedua (pisahkan dengan spasi): ")
    if validasi(teks2):
        break
    print("Input tidak valid!")


t1 = string_ke_tuple(teks1)
t2 = string_ke_tuple(teks2)

gabungan = t1 + t2
tanpa_duplikat = hapus_duplikat(gabungan)
hasil = urut_desc(tanpa_duplikat)

print("\nTuple pertama :", t1)
print("Tuple kedua   :", t2)
print("Hasil akhir   :", hasil)
