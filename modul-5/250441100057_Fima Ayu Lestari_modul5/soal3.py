def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
   
    if jabatan.lower() == "manager":
        tunjangan = 10/100 * gaji_pokok
    elif jabatan.lower() == "staff":
        tunjangan = 5/100 * gaji_pokok
    else:
        tunjangan = 0

    pajak = 5/100 * gaji_pokok

    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("\n=== Rincian Gaji Karyawan ===")
    print("Nama Karyawan  :", nama)
    print("Jabatan       :", jabatan)
    print("Gaji Pokok    : Rp", gaji_pokok)
    print("Tunjangan     : Rp", tunjangan)
    print("Pajak (5%)    : Rp", pajak)
    print("----------------------------")
    print("Gaji Bersih   : Rp", gaji_bersih)
    print("============================\n")

nama_input = input("Masukkan nama karyawan: ")
jabatan_input = input("Masukkan jabatan karyawan (Manager/Staff/Other): ")
gaji_input = float(input("Masukkan gaji pokok karyawan: Rp "))

hitung_gaji_bersih(nama_input, jabatan_input, gaji_input)
