#soal3
jumlah_baris = int(input("Masukkan jumlah baris: "))
for nomor_baris in range(1, jumlah_baris + 1):
    #kirinya
    for angka_kiri in range(1, nomor_baris + 1):
        print(angka_kiri, end="")
    #tebgahnya
    for spasi in range((jumlah_baris - nomor_baris) * 2):
        print(" ", end="")
    #kanannya
    for angka_kanan in range(nomor_baris, 0, -1):
        print(angka_kanan, end="")
    print()