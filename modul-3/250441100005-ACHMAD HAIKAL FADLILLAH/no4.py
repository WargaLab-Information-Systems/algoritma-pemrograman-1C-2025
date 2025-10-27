while True:
    print("selamat datang di IndoMei, selamat berbelanja")
    nama = str(input("masukkan nama anda: "))
    total = 0
    daftarbarang = []
    daftarharga =[]

    while True:
        print("masukkan 'selesai' jika tidak ada tambahan")
        barang = str(input("barang apa yang anda beli: "))
        if barang == "selesai" :
            break
        harga = int(input("masukkan harga barang: "))
        daftarbarang.append(barang)
        daftarharga.append(harga)
    total = sum(daftarharga)

    print("\n==STRUK PEMBELIAN==")
    print("dengan nama: ", nama)
    print("list barang: ")
    for i in range (len(daftarbarang)):
        print(f"{i+1}. {daftarbarang[i]} Rp {daftarharga[i]}")
    print("total harga yang harus anda bayar: ", total)
    print("Terima kasih telah berbelanja di IndoMei!")
    lagi = (input("apakah ada pembeli lagi (y/n): "))
    if lagi == "y" :
        continue
    elif lagi == "n" :
        break
    else:
        print("maaf terjadi kesalahan")