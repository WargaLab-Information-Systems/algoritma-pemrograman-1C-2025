def cek_anagram(kata1, kata2):

    huruf_1 = sorted(kata1)
    huruf_2 = sorted(kata2)

    return huruf_1 == huruf_2

kata_a = input("Masukkan kata pertama (huruf kecil, tanpa spasi): ")
kata_b = input("Masukkan kata kedua (huruf kecil, tanpa spasi): ")

hasil_anagram = cek_anagram(kata_a, kata_b)

print("-" * 30)
if hasil_anagram:
    print(f"'{kata_a}' dan '{kata_b}' adalah *Anagram*! (True)")
else:
    print(f"'{kata_a}' dan '{kata_b}' BUKAN Anagram. (False)")
print("-" * 30)