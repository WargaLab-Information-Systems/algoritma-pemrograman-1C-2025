t1 = tuple(map(int, input("Masukkan angka untuk tuple pertama (pisahkan dengan spasi): ").split()))
t2 = tuple(map(int, input("Masukkan angka untuk tuple kedua (pisahkan dengan spasi): ").split()))

gabung = t1 + t2

angka = []
for x in gabung:
    if x not in angka:
        angka.append(x)

for i in range(len(angka)):
    for j in range(0, len(angka) - i - 1):
        if angka[j] < angka[j + 1]:
            angka[j], angka[j + 1] = angka[j + 1], angka[j]

hasil = tuple(angka)

print("t1 : ", t1)
print("t2 : ", t2)
print("Hasil akhir : ", hasil)
