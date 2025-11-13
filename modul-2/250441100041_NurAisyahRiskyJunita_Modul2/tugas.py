


# # TUGAS NOMOR 1

# # Menghitung jumlah dan harga satuan buku dan pensil
# buku = 3 * 5000
# pensil = 2 * 4500
# total = buku + pensil

# # Menghitung pajak
# pajak = total * 0.10
# total_bayar = total + pajak

# # Tampilkan hasil
# print("Total belanja sebelum pajak:", total)
# print("Pajak 10%:", pajak)
# print("Total yang harus dibayar:", total_bayar) 




# # TUGAS NOMOR 2

# # Program menghitung volume dan luas permukaan balok

# # Input dari user
# panjang = float(input("Masukkan panjang balok (cm): "))
# lebar = float(input("Masukkan lebar balok (cm): "))
# tinggi = float(input("Masukkan tinggi balok (cm): "))

# # Hitung volume
# volume = panjang * lebar * tinggi

# # Hitung luas permukaan
# luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# # Tampilkan hasil
# print("\n=== Hasil Perhitungan Balok = ==")
# print("Volume balok        :", volume, "cm³")
# print("Luas permukaan balok:", luas_permukaan, "cm²")

# TUGAS NOMOR 3

#tb: total bola
#a: jumlah bola yang diambil

merah = int(input("masukkan angka:"))
biru = int(input("masukkan angka:"))
tb = merah + biru
a = int(input("masukan angka:"))


faktorial_a = tb * (tb-1) * (tb-2) 
faktorial_b = a * (a-1) * (a-2)

kombinasi = faktorial_a // faktorial_b

print("faktorial_a: ",(faktorial_a))
print("faktorial_a:",(faktorial_b))
print("kemungkinan kombinasi:",(kombinasi))