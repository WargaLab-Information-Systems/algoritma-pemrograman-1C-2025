def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0
    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("RINCIAN GAJI KARYAWAN")
    print(f"nama karyawan: {nama}")
    print(f"jabatan: {jabatan}")
    print(f"gaji pokok: Rp {gaji_pokok:,.2f}")
    print(f"tunjangan: Rp {tunjangan:,.2f}")
    print(f"pajak (5%): Rp {pajak:,.2f}")
    print(f"gaji bersih: Rp {gaji_bersih:,.2f}")
    return gaji_bersih

print("GAJI BERSIH KARYAWAN")
nama = input("masukkan nama karyawan: ")
jabatan = input("masukkan jabatan (manager/staff): ")
gaji_pokok = float(input("masukkan gaji pokok: "))

gaji_bersih = hitung_gaji(nama, jabatan, gaji_pokok)