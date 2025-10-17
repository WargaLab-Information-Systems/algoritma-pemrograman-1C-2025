# tb: total bola
# a: jumlah bola yang diambil
tb = 14
a = 3

# menghitung kombinatorik agar nilai r = 3
numerator = tb * (tb-1) * (tb-2)        # 14*13*12 = 2184
denominator = a * (a-1) * (a-2)      # 3*2*1 = 6

kombinasi = numerator // denominator

print(f"dumerator: {numerator}")
print(f"denominator: {denominator}")
print(f"kemungkinan kombinasi: {kombinasi}")