def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    if jabatan.lower() == "manager":
        tunjangan = gaji_pokok * 0.10  # 10%
    elif jabatan.lower() == "staff":
        tunjangan = gaji_pokok * 0.05  # 5%
    else:
        tunjangan = 0  # selaain manager  dan staff ga dapet tunjangan
    
    # pajak 5%
    pajak = gaji_pokok * 0.05
    
    # hitung gaji bersih
    gaji_bersih = gaji_pokok + tunjangan - pajak
    
    # tampilkan hasil
    print(f"\n=== SLIP GAJI KARYAWAN ===")
    print(f"Nama          : {nama}")
    print(f"Jabatan       : {jabatan}")
    print(f"Gaji Pokok    : Rp {gaji_pokok:,}")
    print(f"Tunjangan     : Rp {tunjangan:,}")
    print(f"Pajak (5%)    : Rp {pajak:,}")
    print(f"Gaji Bersih   : Rp {gaji_bersih:,}")
    
    return gaji_bersih

# program utama
print("=== PROGRAM HITUNG GAJI BERSIH ===")

while True:
    print("\n--- DATA KARYAWAN ---")
    
    nama = input("Nama karyawan    : ")
    jabatan = input("Jabatan (Manager/Staff/lain): ")
    gaji_pokok = float(input("Gaji pokok      : Rp "))
    
    # Hitung gaji bersih
    hitung_gaji_bersih(nama, jabatan, gaji_pokok)
    
    #loop bila lanjut
    lanjut = input("\nHitung gaji lagi? (y/n): ").lower()
    if lanjut != 'y':
        print("yawdah klo ga mw")
        break

