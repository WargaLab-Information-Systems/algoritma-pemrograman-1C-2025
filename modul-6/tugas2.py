t1 = (3, 1, 4)
t2 = (1, 5, 9)

gabung = t1 + t2

unik = []
for i in gabung:
    if i not in unik:
        unik.append(i)

for i in range(len(unik)):
    for j in range(i + 1, len(unik)):
        if unik[i] < unik[j]:
            unik[i], unik[j] = unik[j], unik[i]

hasil = tuple(unik)

print("hasil akhir:", hasil)