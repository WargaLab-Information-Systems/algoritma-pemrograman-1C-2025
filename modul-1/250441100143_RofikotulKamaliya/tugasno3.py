# Soal No.3

total_bola = int(input("Masukkan total bola: "))
bola_diambil = int(input("Masukkan jumlah bola yang diambil: "))

numerator = total_bola * (total_bola-1) * (total_bola-2)        
denominator = bola_diambil * (bola_diambil-1) * (bola_diambil-2)      

kombinasi = numerator // denominator

print(f"numerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")