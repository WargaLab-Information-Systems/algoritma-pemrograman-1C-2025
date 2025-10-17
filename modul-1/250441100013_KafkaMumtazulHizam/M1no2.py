p = int(input("masukan panjang: "))
l = int(input("masukan lebar: "))
t = int(input("masukan tinggi: "))

volume = p * l * t
luas = 2 * (p * l + p * t + l * t)

print(f"Volume balok    : {volume}")
print(f"Luas permukaan  : {luas}")