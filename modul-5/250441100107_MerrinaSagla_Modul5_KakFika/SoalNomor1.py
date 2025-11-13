#FUNGSI REKURSIF UNTUK MENGHTUNG FAKTORIAL
def faktorial (n):
    if n==0 or n == 1: #digunakan n==0 atau n==1 karena faktorial 0 dan 1 adalah 1
        return 1  
    else:
        return n*faktorial(n-1) #pemanggilan fungsi rekursif
    
#PROGRAM UTAMA
N = int (input("Masukkan Bilangan bulat Non-negatif:"))
if N <0: # n<0 berarti bilangan negatif
    print ("angka harus non-negatif")
else : 
    hasil = faktorial(N) #mengambil nilai kembalian dari fungsi faktorial
    print(f"faktorial dari {N}adalah {hasil}")