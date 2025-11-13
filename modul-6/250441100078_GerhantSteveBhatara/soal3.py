#membuat deretan angka untuk memeriksa apakah deretan tersebut dapat dibagi menjadi dua bagian
def cek_sama_bagi(daftar): #fungsi untuk memeriksa apakah daftar dapat dibagi menjadi dua bagian dengan jumlah yang sama
    total = sum(daftar)

    if total % 2 != 0: # jika total tidak genap, tidak bisa dibagi sama sehingga langsung salah
        return False
    
    target = total // 2 # target jumlah untuk setiap bagian
    jumlah = 0
    
    for angka in daftar: #iterasi melalui setiap angka dalam daftar
        jumlah += angka #menambahkan angka ke jumlah saat ini
        if jumlah == target:
            return True
    return False

data = [] #list kosong untuk menyimpan data angka

while True: #loop utama program
    print("\n===== MENU CRUD =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cek Apakah Bisa Dibagi Sama")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ") #menerima input pilihan dari pengguna

    if pilihan == '1': #menambah data baru
        nilai = int(input("Masukkan angka: "))
        data.append(nilai) #menambahkan nilai ke dalam daftar
        print("Data berhasil ditambahkan!")

    elif pilihan == '2': #menampilkan data saat ini
        print("Data saat ini:", data)

    elif pilihan == '3':
        indeks = int(input("Masukkan indeks data yang ingin diubah: "))
        if 0 <= indeks < len(data):
            nilai_baru = int(input("Masukkan nilai baru: "))
            data[indeks] = nilai_baru
            print("Data berhasil diubah!")
        else:
            print("Indeks tidak valid!")

    elif pilihan == '4':
        indeks = int(input("Masukkan indeks data yang ingin dihapus: "))
        if 0 <= indeks < len(data): #menghitung bayak elemen
            data.pop(indeks) #menghapus elemen pada indeks tertentu
            print("Data berhasil dihapus!")
        else:
            print("Indeks tidak valid!")

    elif pilihan == '5':
        if cek_sama_bagi(data): #memanggil fungsi untuk memeriksa apakah data dapat dibagi menjadi dua bagian dengan jumlah yang sama
            print(" TRUE, Data dapat dibagi menjadi dua bagian dengan jumlah sama.")
        else:
            print(" FALSE, Data TIDAK dapat dibagi menjadi dua bagian dengan jumlah sama.")

    elif pilihan == '6':
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")