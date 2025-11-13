nama = input("masukkan nama karyawan: ")
jabatan = input("masukkan jabatan (manager/staff): ")
gaji_pokok = float(input("masukkan gaji pokok: "))

def hitung_gaji(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok

    if jabatan == "manager" :
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff" :
        tunjangan = 0.05 * gaji_pokok
    else:
        tunjangan = 0
    
    gaji_bersih = gaji_pokok + tunjangan - pajak

    print("=== Rincian Gaji Karyawan ===")
    print(f"nama karyawan: {nama}")
    print(f"jabatan: {jabatan}")
    print(f"gaji pokok: Rp {gaji_pokok:,.0f}")
    print(f"tunjangan: Rp {tunjangan:,.0f}")
    print(f"pajak(5%): Rp {pajak:,.0f}")
    print(f"gaji bersih: Rp {gaji_bersih:,.0f}")
    print("=========================")

hitung_gaji(nama, jabatan, gaji_pokok)
  
