while True:
    print("=== PEMBELI ===")
    nama = input("nama pembeli: ")
    barang_harga = []
    total = 0
    
    while True:
        barang = input("masukkan nama barang, ketik 'selesai' kalo udah: ")
        if barang == 'selesai': #kalo ga bisa, tambahin aja .lower() di bagian if barag biar ga di hitung nama barang
            break
        harga = int(input("masukkan harga barang: "))
        barang_harga.append (barang, harga)
        total += harga
    
    # struknya gais
    print(f"==== STRUK PEMBELIAN {nama} ====")
    for barang, harga in barang_harga:
        print(f"{barang}: Rp {harga}")
    print(f"total pesanan: Rp {total}")
    print("terimakasih sudah berbelanja di IndoMei.") 
    print(barang_harga)
    
    if input("apakah ada pembeli berikutnya? (y/n): ") != "y":#bisa juga pakek !=n
        break