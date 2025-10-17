#rumus balok
panjang = int(input("Masukkan panjang balok: ")) #variabel panjang balok
lebar = int(input("Masukkan lebar balok: ")) #variabel lebar balok
tinggi = int(input("Masukkan tinggi balok: ")) #variabel tinggi balok
luas_permukaan = 2 * panjang * lebar + 2 * panjang * tinggi + 2 * lebar * tinggi 
volume = panjang * lebar * tinggi #rumus volume balok
print("luas permukaan baloknya adalah:", luas_permukaan) #mencetak hasil luas permukaan balok
print("Volume baloknya adalah:", volume) #mencetak hasil volume balok