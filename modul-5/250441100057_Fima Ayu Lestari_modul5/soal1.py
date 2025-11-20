def hitung_faktorial(angka):
    if angka <= 1:
        return 1
    else:
        return angka * hitung_faktorial(angka - 1)

while True:
    n = input("Masukkan angka: ")

    if n.lstrip('-').isdigit():
        n = int(n)
        if n < 0:
            print("Angka tidak boleh negatif. Silakan coba lagi.")
        else:
            hasil = hitung_faktorial(n)
            print("Faktorial dari", n, "adalah", hasil)
            break
    else:
        print("Input harus berupa angka! Silakan coba lagi.")
