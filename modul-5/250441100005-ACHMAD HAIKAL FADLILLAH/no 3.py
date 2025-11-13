def hitung(jabatan, gaji):
    pajak = 5/100 * gaji

    if jabatan == "manajer":
        tunjangan = 10/100 * gaji
    elif jabatan == "staf":
        tunjangan = 5/100 * gaji
    else:
        tunjangan = 0
        print("tidak ada tunjangan karena anda bukan staf atau manajer")

    gaji_bersih = gaji + tunjangan - pajak

    print("potongan pajak: ", pajak)
    print("tunjangan anda: ", tunjangan)
    print("gaji bersih: ", gaji_bersih)

nama = input("masukkan nama anda: ")
gaji = int(input("masukkan gaji pokok anda: "))
jabatan = input("masukkan jabatan anda: ")

hitung(jabatan, gaji)