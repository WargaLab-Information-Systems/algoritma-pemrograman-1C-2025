# soal 3
#tb: total bola
#a: jumlah bola yang diambil

merah = int(input("masukkan jumlah bola merah:"))
biru = int(input("masukkan jumlah bola biru:"))
tb=merah + biru
a=3

numerator= tb * (tb-1) * (tb-2)
denominator = a * (a-1) * (a-2)

kombinasi = numerator // denominator

print(f"numerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")