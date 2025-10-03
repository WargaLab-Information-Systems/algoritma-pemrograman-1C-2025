bola_merah=int(8)
bola_biru=int(6)

n = bola_biru+bola_merah  # total bola
r = int(3)

kombinasi = (n * (n-1) * (n-2)) // (r * (r-1) * (r-2))
print("Jumlah kombinasi:", kombinasi) 