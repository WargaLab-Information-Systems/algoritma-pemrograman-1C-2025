def hitung_faktorial(bilangan_masuk):
    if bilangan_masuk <= 1:
        return 1
    return bilangan_masuk * hitung_faktorial(bilangan_masuk - 1)
bilangan_input = int(input("masukkan bilangan non-negatif: "))
if bilangan_input < 0:
    print("Error: nggak bisa negatif")
else:
    hasil_faktorial = hitung_faktorial(bilangan_input)
    print("Hasil faktorial dari", bilangan_input, "adalah", hasil_faktorial)





