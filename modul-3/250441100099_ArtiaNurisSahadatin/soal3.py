#==NO3==
#menganalisa kalimat dengan menampilkan jumlah huruf vokal dan konsona dan jumlah kata
# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal dan konsonan
vokal = "aeiouAEIOU"
konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_kata = 0
panjang = len(kalimat) #len di gunakan u/ mengetahui brapa banyak karakter yang ada di dalamnya
kata_sedang_berjalan = False

for i in range(panjang):
    huruf = kalimat[i]

    # Hitung vokal dan konsonan jika huruf ada pada list
    if huruf in vokal:
        jumlah_vokal += 1
    elif huruf in konsonan:
        jumlah_konsonan += 1

    # Hitung kata dengan cara mendeteksi transisi dari non-spasi ke spasi atau akhir kalimat
    if huruf != ' ' and not kata_sedang_berjalan:
        kata_sedang_berjalan = True
        jumlah_kata += 1
    elif huruf == ' ':
        kata_sedang_berjalan = False

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)