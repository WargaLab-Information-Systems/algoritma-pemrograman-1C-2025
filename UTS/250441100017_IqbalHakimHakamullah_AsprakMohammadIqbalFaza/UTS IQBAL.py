# print("SELAMAT DATANG DI PENYEWAAN MOTOR ACONK")
# print("PILIH JENIS MOTOR YANG INGIN ANDA SEWA")
# a = print("1. MOTOR MATIC RP. 50.000.00")
# b = print("2. MOTOR TRAIL RP. 100.000.00")
# c = print("3. MOTOR SPORT RP. 75.000.00")
# pilihan = int(input("motor mana yang akan anda sewa? pilih angka(1,2,3)"))
# for i in a :
#     if pilihan != "1,2,3":
#         print("HARUS MENGINPUT ANGKA!!!")
#         break
#     else:
#         print(f"anda memilih {pilihan} ")
#         (str(input"berapa lama anda akan menyewa?(dalam hari)"))

print("selamat datang di sewa motor aconk")
print("berikut adalah daftar motor yang kami sewakan")
print("a. motor matic")
print("b. motor trail")
print("c. motor sport")
pilihan = str(input("pilih nomor mana yang membuat anda tertarik (a,b,c)"))
while True:
    if pilihan == 'a' :
        print("motor matik ini memiliki harga sewa Rp.50.000.00")
    elif pilihan == 'b' :
        print("motor trail ini memiliki harga sewa Rp.100.000.00")
    elif pilihan == 'c' :
        print("motor sport ini memiliki harga Rp. 75.000.00")
    else:
        print("HARUS MEMILIH")
    break

harga = 0
lama_sewa = input("berapa lama anda berncana menyewa?")
if lama_sewa > 3:
    print("anda mendapatkan asuransi per 3 hari sewa dan berlaku kelipatan!")
    lama_sewa += harga
else:
    pass