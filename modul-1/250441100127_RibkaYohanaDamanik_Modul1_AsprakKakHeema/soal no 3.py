if n == 14 and r == 3:
    faktorial_n = 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    faktorial_r = 3 * 2 * 1
    faktorial_nr = 11* 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

    kombinasi = faktorial_n // (faktorial_r * faktorial_nr)

    print("jumlah kemungkinan kombinasi bola :", kombinasi)
else:
    print("program hanya mendukung input m=14 dan r=3 sesuai soal.")
