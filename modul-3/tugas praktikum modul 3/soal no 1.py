def tampilkan_bilangan_prima(n):
   
    """
    menampilkan bilangan prima dari 1 sampai n.
    """
    if n < 2:
        print("tidak ada bilangan prima dalam rentang ini.")
        return
    print(f"bilangan prima dari 1 sampai {n} adalah:")

    for num in range(2, n + 1):
        is_prima = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                id_prima = False
                break
        if is_prima:
            print(num, end=" ")
    print()

n = int(input("masukkan nilai n: "))
tampilkan_bilangan_prima(n)