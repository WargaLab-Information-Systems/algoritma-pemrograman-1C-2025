while True:
    print("Selamat datang di IndoMei")
    nama_pembeli=str(input("input nama = "))
    print(nama_pembeli)
    barang_list=[]
    harga_list=[]
    total=0

    while True:
        validasi_barang=str(input("Nama barang / 'selesai' untuk mengakhiri ")) 
        if validasi_barang=="selesai":
            break
        harga=int(input("Harga barang"))
        barang_list.append(validasi_barang)
        harga_list.append(harga)
        total=sum(harga_list)

    print("======== STRUK PEMBAYARAN ========")
    print("nama pembeli = ",nama_pembeli)
    print(f"total yang harus di bayar = {total}")
    print("daftar barang yang di beli ",barang_list)
    
    lanjut=str(input("apakah ada pembeli selanjutnya ? Y = lanjut or N = berhenti"))
    if lanjut=="Y" or lanjut=="y":
        continue
    else:
        print("program selesai")
        break