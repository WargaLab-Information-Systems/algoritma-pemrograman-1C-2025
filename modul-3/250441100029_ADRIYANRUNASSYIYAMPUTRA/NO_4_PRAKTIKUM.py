while True:
    nama_pembeli=str(input("input nama = "))
    barang_list=[]
    harga_list=[]
    total=0

    while True:
        print(f"keranjang = {barang_list} harga = {harga_list}")
        v_barang=str(input("Nama barang / ketik 'selesai' untuk mengakhiri =  "))
        if v_barang=="selesai":
            break
        harga=int(input("Harga barang"))
        barang_list.append(v_barang)
        harga_list.append(harga)
        total=sum(harga_list)

    print("======== STRUK PEMBAYARAN =======")
    print("                                 ")
    print("nama = ",nama_pembeli)
    print(f"total pembayaran = {total}")
    print("list barang yang di beli ",barang_list)#looping
    for i, barang in enumerate(barang_list, 1):
        print(f"[{i}. '{barang}']")
    print("                                  ")
    print("==================================")
    
    lanjut=str(input("apakah ada pembeli selanjutnya ? Y = lanjut or N = berhenti "))
    if lanjut=="Y" or lanjut=="y":
        continue
    else:
        print("program selesai")
        break