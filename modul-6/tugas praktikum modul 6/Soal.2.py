def gabung_dan_urutkan_tuple(tuple1, tuple2):
    tuple_gabungan = tuple1 + tuple2

    list_tanpa_duplikat = []
    for item in tuple_gabungan:
        if item not in list_tanpa_duplikat:
            list_tanpa_duplikat.append(item)

    list_tanpa_duplikat.sort(reverse=True)

    return tuple(list_tanpa_duplikat)

input_a = input("masukkan angka untuk tuple pertama: ")
tuple_a = tuple(int(x) for x in input_a.split(','))

input_b = input("masukkan angka untuk tuple kedua: ")
tuple_b = tuple(int(x) for x in input_b.split(','))

hasil = gabung_dan_urutkan_tuple(tuple_a, tuple_b)
print(f"hasil: {hasil}")