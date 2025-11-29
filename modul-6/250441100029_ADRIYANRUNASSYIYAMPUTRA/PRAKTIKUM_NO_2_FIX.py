tupl1=(3,9,7)
tuple2=(2,3,1)
list_gabung=list(tupl1+tuple2)
print("sebelum di ubah = ",list_gabung)
list_sorted=[]
huruf_terbesar=int(0)

for x in tupl1: #pengecekan kesamaan 
    if x in tuple2:
        list_gabung.remove(x)
        print("list gabung sekarang = ",list_gabung)

while len(list_gabung) > 0: 
    huruf_terbesar = 0
    for t in list_gabung:
        if t > huruf_terbesar:
            huruf_terbesar = t
    list_sorted.append(huruf_terbesar)
    list_gabung.remove(huruf_terbesar)

tuple3=tuple(list_sorted)
print("Tuple sekarang = ",tuple3)

