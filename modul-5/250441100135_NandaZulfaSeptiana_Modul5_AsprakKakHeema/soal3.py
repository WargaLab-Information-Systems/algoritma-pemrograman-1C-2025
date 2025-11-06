def hitung_gaji(nama, jabatan, gaji_pokok):
    
    pajak = 0.05
    
    if jabatan == "Manager" or "manager":
        tunjangan = 0.10  
    elif jabatan == "Staff" or "staff":
        tunjangan = 0.05  
    else:
        tunjangan = 0.00 
        
    besar_tunjangan = gaji_pokok * tunjangan
    besar_pajak = gaji_pokok * pajak
    
    gaji_kotor = gaji_pokok + besar_tunjangan
    gaji_bersih = gaji_kotor - besar_pajak
    
    print("-" * 40)
    print("         SLIP GAJI BULANAN         ")
    print("-" * 40)
    print(f"Nama Karyawan: {nama}")
    print(f"Jabatan      : {jabatan}")
    print("-" * 40)
    print(f"Gaji Pokok   : Rp {gaji_pokok:,}")
    print(f"Tunjangan ({int(tunjangan*100)}%): Rp {besar_tunjangan:,}")
    print(f"Potongan PPh (5%): Rp {besar_pajak:,}")
    print("-" * 40)
    print(f"Gaji Bersih  : Rp {gaji_bersih:,}")
    print("-" * 40)
    
    return gaji_bersih

nama_karyawan = input("Masukkan Nama Karyawan : ")
jabatan_karyawan = input("Masukkan Jabatan Karyawan (Manager/Staff/Lainnya) : ")
gaji_pokok_karyawan = float(input("Masukkan Gaji Pokok Bulanan : "))

gaji_akhir = hitung_gaji(nama_karyawan, jabatan_karyawan, gaji_pokok_karyawan)