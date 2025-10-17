panjang = int(input("panjang "))
lebar = int(input("lebar "))
tinggi = int(input("tinggi "))
v = panjang * lebar * tinggi

print("V = P * L * T")
print("volume: ", v)

lp = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
print("L.P = (P * L) + (P * T) + (L * T)")
print("luas permukaan balok: ", lp)