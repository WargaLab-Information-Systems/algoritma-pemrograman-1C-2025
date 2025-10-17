# a = total bola yang diambil
total_bola = 14
a = 3

# menghhitung kombinasi
numerator = total_bola * (total_bola - 1) * (total_bola - 2)
denominator = a * (a - 1) * (a - 2)

kombinasi = numerator / denominator

print("HASIL")
print(f"numerator= {numerator}")
print(f"denominator= {denominator}")
print(f"jadi, kombinasi yang didapat adalah= {kombinasi}")
print(f"yang berarti ada {kombinasi} yang dapat digunakan")