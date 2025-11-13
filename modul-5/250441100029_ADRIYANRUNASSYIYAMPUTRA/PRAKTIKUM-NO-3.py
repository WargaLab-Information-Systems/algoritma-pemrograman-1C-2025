def hitung_gaji(nama,jabatan,gajipokok):

    if jabatan=="manager":#pengecekan kondisi untuk jabatan
        tunjangan=0.10
    elif jabatan=="staff":
        tunjangan=0.05
    else:
        pass
    
    penghitungan_pph=gajipokok*5//100 # penghitungan pph
    tunjangan=gajipokok*tunjangan #penghitungan tunjangan
    gajibersih=(gajipokok+tunjangan)-penghitungan_pph # penghitungan gajibersih
    print("nama karyawan = ",nama)
    print("jabatan = ",jabatan)
    print("total gaji pokok = ",gajipokok)
    return gajibersih

nama=str(input("input nama = "))
jabatan=str(input("input jabatan manager/staff = "))
while jabatan != 'manager' and jabatan != 'staff': 
    print("Input dengan benar dan perhatikan huruf kecil dan besar!!")
    jabatan = str(input("Input jabatan = "))

gaji_pokok=int(input("input gaji = "))

hasil=hitung_gaji(nama,jabatan,gaji_pokok) #pemanggilan fungsi 
print(hasil)
print(hitung_gaji(nama,jabatan,gaji_pokok))