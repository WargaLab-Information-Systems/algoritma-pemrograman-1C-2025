def hitung_gaji(nama, jabatan, gaji_pokok):
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0
    pajak = 0.05 * gaji_pokok
    gaji_bersih = gaji_pokok - pajak + tunjangan

    print("\n=== Rincian Gaji Karyawan ===")
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp {gaji_pokok:,.0f}")
    print(f"Tunjangan     : Rp {tunjangan:,.0f}")
    print(f"Pajak PPh (5%): Rp {pajak:,.0f}")
    print(f"Gaji Bersih   : Rp {gaji_bersih:,.0f}")

print("Masukkan data karyawan:")
nama = input("Nama Karyawan: ")
jabatan = input("Jabatan (manager/staff): ")
gaji_pokok = float(input("Gaji Pokok: "))
hitung_gaji(nama, jabatan, gaji_pokok)