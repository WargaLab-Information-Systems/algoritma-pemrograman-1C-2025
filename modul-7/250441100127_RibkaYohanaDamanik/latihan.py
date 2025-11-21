# makanan = {"nama":[nasi_goreng,nasi_padang]}

# makanan = input("masukkan nama makanan:")
# print ("\n===daftar menu===")
# print ("1.Tampilkan nama makanan")
# print ("2.Tambah makanan")
# print ("3.keluar")

# pilihan = input("pilih menu:")

# if pilhan == "1":
#     if not makanan:
#         print ("makanan tidak ada")
#     else: 
#         tambahan.append = tambah_namamakanan
#         print("makanantambahan")
#revisi
# Program daftar makanan sederhana menggunakan dictionary

makanan = {}  

while True:
    print("\n=== MENU ===")
    print("1. Tampilkan nama makanan")
    print("2. Tambah menu makanan")
    print("3. Keluar")
    
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if not makanan:
            print("Belum ada makanan yang ditambahkan.")
        else:
            print("Daftar makanan:")
            for nama in makanan:
                print("-", nama)
                
    elif pilihan == "2":
        nama_baru = input("Masukkan nama makanan baru: ")
        if nama_baru in makanan:
            print(f"{nama_baru} sudah ada di daftar.")
        else:
            makanan[nama_baru] = None  
            print(f"{nama_baru} berhasil ditambahkan.")
            
    elif pilihan == "3":
        print("Keluar dari program.")
        break
        
    else:
        print("Menu tidak valid, coba lagi.")
