# program penghitung biaya parkir mall
#Tarif parkir
tarif_2jam_pertama = 5000
tarif_perjam = 3000
maksimal_harian = 20000

lama_parkir = int(input("Masukkan lama parkir(jam):"))
statu_vip = input("Apakah anda member VIP?(ya/tidak):")

#menghitung biaya
if "status_vip" == "ya" : 
    biaya = 0
else:
    if lama_parkir <= 2:
        biaya = tarif_2jam_pertama
    else:
        biaya = 5000 + (lama_parkir - 2) * 3000
    # batasi maksimal harian 
    biaya = min(biaya,maksimal_harian)    

#output
print("Total biaya parkir: Rp", biaya)