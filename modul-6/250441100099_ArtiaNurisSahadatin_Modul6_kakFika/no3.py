# #membuat deretan angka untuk memeriksa apakah deretan tersebut dapat dibagi menjadi dua bagian
# def cek_sama_bagi(daftar):
#     total = sum(daftar)

#     if total % 2 != 0:
#         return False
    
#     target = total // 2
#     jumlah = 0
    
#     for angka in daftar:
#         jumlah += angka
#         if jumlah == target:
#             return True
#     return False

# data = []

# while True:
#     print("\n===== MENU CRUD =====")
#     print("1. Tambah Data")
#     print("2. Tampilkan Data")
#     print("3. Ubah Data")
#     print("4. Hapus Data")
#     print("5. Cek Apakah Bisa Dibagi Sama")
#     print("6. Keluar")

#     pilihan = input("Pilih menu (1-6): ")

#     if pilihan == '1':
#         nilai = int(input("Masukkan angka: "))
#         data.append(nilai)
#         print("Data berhasil ditambahkan!")

#     elif pilihan == '2':
#         print("Data saat ini:", data)

#     elif pilihan == '3':
#         indeks = int(input("Masukkan indeks data yang ingin diubah: "))
#         if 0 <= indeks < len(data):
#             nilai_baru = int(input("Masukkan nilai baru: "))
#             data[indeks] = nilai_baru
#             print("Data berhasil diubah!")
#         else:
#             print("Indeks tidak valid!")

#     elif pilihan == '4':
#         indeks = int(input("Masukkan indeks data yang ingin dihapus: "))
#         if 0 <= indeks < len(data): # len = menghitung bayak elemen
#             data.pop(indeks)
#             print("Data berhasil dihapus!")
#         else:
#             print("Indeks tidak valid!")

#     elif pilihan == '5':
#         if cek_sama_bagi(data):
#             print(" TRUE, Data dapat dibagi menjadi dua bagian dengan jumlah sama.")
#         else:
#             print(" FALSE, Data TIDAK dapat dibagi menjadi dua bagian dengan jumlah sama.")

#     elif pilihan == '6':
#         print("Program selesai. Terima kasih!")
#         break

#     else:
#         print("Pilihan tidak valid, coba lagi.")


nama_list= [1],[2],[3],[4]
nama_list = []