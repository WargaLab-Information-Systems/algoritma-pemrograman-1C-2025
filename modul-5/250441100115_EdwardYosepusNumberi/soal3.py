def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    
    tunjangan = 0.1 * gaji_pokok if jabatan.lower() == 'manager' else 0.05 * gaji_pokok
    
    pajak = 0.05 * gaji_pokok
  
    gaji_bersih = gaji_pokok + tunjangan - pajak
   
    print(f"Nama        : {nama}")
    print(f"jabatan     : {jabatan}")
    print(f"tunjangan   : {tunjangan:,.0f}")
    print(f"pajak       : {pajak:,.0f}")
    print(f"gaji berish : {gaji_bersih:,.0f}")

nama = input("Nama: ")
jabatan = input("Jabatan (Manager/Staff): ")
gaji_pokok = float(input("Gaji Pokok: "))
hitung_gaji_bersih(nama, jabatan, gaji_pokok)