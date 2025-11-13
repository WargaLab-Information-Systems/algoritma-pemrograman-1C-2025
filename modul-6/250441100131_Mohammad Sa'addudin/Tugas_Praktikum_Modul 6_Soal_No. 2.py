def combine_and_sort(t1, t2):
    combined = t1 + t2

    tanpa_duplikat = []

    for angka in combined:
        if angka not in tanpa_duplikat:
            tanpa_duplikat.append(angka)

    for i in range(len(tanpa_duplikat)):
        for j in range(i + 1, len(tanpa_duplikat)):
            if tanpa_duplikat[j] > tanpa_duplikat[i]:
                tanpa_duplikat[i], tanpa_duplikat[j] =  tanpa_duplikat[j], tanpa_duplikat[i]

    return tuple(tanpa_duplikat)

n1 = int(input("berapa jumlah angka pada tuple pertama "))
list1 = []
for i in range(n1):
    angka = int(input(f"masukkan angka ke-{i+1}: "))
    list1.append(angka)
t1 = tuple(list1)

n2 = int(input("berapa jumlah angka pada tuple kedua. "))
list2 = []
for i in range(n2):
    angka = int(input(f"masukkan angka ke-{i+1}: "))
    list2.append(angka)
t2 = tuple(list2)

hasil = combine_and_sort(t1, t2)
print("hasil akhir: ", hasil)