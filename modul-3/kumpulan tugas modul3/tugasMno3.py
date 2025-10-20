# Program analisis kalimat

kalimat = input("Masukkan sebuah kalimat: ").lower()

vokal = "aiueo"
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)
jumlah_konsonan = sum(1 for huruf in kalimat if huruf.isalpha() and huruf not in vokal)
jumlah_kata = len(kalimat.split())

print(f"Jumlah huruf vokal   : {jumlah_vokal}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")
print(f"Jumlah kata          : {jumlah_kata}")
