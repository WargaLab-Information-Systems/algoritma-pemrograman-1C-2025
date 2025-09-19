# Tugas Pertemuan 1 

# Soal Pertama
nama = "denis saputra"        # string
nim = "240441100029"    # NIM jadi string
sks = 144              # integer
status = True           # boolean (True = Aktif dan False = Tidak Aktif)
ipk = 3.2              # float

print(nama, nim, sks, status, ipk)

# Soal Kedua
jumlah_barang = "5"
harga_satuan = 15000

# Ini Sebelum Diubah int
total_sementara = jumlah_barang * 2
print("total sementara:", total_sementara)

# Ini Setelah Diubah int
jumlah_barang = int(jumlah_barang)
total_akhir = jumlah_barang * harga_satuan
print("total akhir:", total_akhir)

# Soal Ketiga
hasil = 10 + 5 * 2 - 12 / 6 % 3
print("Hasil:", hasil)

# Soal Keempat
masa_studi = 8
ipk_mhs = 3.1
ada_nilai_e = False

lulus_tepat_waktu = (masa_studi <= 8) and (ipk_mhs >= 3.00) and (ada_nilai_e == False)
print("Lulus Tepat Waktu:", lulus_tepat_waktu)
