kalimat = str(input("masukkan kalimat: "))
vokal = 0
konsonan = 0
hurufvokal = "aiueoAIUEO"
space = " "

for huruf in kalimat :
        if huruf in hurufvokal :
            vokal += 1
        elif huruf in space :
            space 
        else:
            konsonan += 1

jumlahkata = len(kalimat.split())
print("jumlah huruf vokal: ", vokal)
print("jumlah huruf konsonan: ", konsonan)
print("jumlah kata pada kalimat: ", jumlahkata)