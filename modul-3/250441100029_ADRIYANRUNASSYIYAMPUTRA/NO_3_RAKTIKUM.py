total_vokal = 0
total_konsonan = 0
space = " ",
hurufvokal = ["a","i","u","e","o","A","I","U","E","O"]
kalimat = str(input("masukkan kalimat: "))


for huruf in kalimat :
        if huruf in hurufvokal :
            total_vokal += 1
        elif huruf in space :
            pass 
        else:
            total_konsonan += 1

jumlahkata = len(kalimat.split())

print(f"kalimat : {kalimat}")
print("jumlah kata = : ", jumlahkata)
print(f"total huruf vokal =  ", total_vokal)
print("jumlah huruf konsonan: ", total_konsonan)
