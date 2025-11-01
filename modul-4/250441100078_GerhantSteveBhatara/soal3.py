n = int(input("Masukkan jumlah baris (n): "))
#perulangan utama loop luar
for i in range(n, 0, -1):
#mencetak angka naik sisi kiri
    for j in range(1, i + 1):
        print(j, end="")
#mencetak spasi tengah
    for spasi in range(2 * (n - i)):
        print(" ", end="")
#menecetak angka menurun sisi kanan
    for k in range(i, 0, -1):
        print(k, end="")
#pindah ke baris baru
    print()


# n = int(input("Masukkan jumlah baris (n): "))
# #perulangan loop luar
# for i in range(1, n + 1):
# #spasi kiri
#     for kiri in range(n - i):
#         print(" ", end="")
# #spasi tengah
#     for tengah in range(1, i + 1):
#         print(tengah, end=" ")
#     print()+