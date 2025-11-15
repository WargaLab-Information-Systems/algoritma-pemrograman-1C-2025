print("Masukkan angka-angka pertama (pisahkan dengan spasi):")
data1 = input() 
t1 = [int(x) for x in data1.split()] 

print("Masukkan angka-angka kedua (pisahkan dengan spasi):")
data2=input()
t2 = [int(x) for x in data2.split()] 

_join = t1 + t2 

ririn = []
for angka in _join:
    if angka not in ririn:
        ririn.append(angka)

n = len(ririn) 
for i in range(n):
    for j in range(0, n - i - 1):
        if ririn[j]< ririn[j + 1]:
            # Tukar posisi
            temp = ririn[j]
            ririn[j] = ririn[j + 1]
            ririn[j + 1] = temp

print("Hasil akhir dari penggabungan dan pengurutan adalah:")
print(ririn)
