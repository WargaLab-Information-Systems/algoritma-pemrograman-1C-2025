def is_anagram(k1, k2):
    return sorted(k1) == sorted(k2)

a = input("Kata 1: ")

# Cek hanya huruf
if not a.isalpha():
    print("Input tidak boleh mengandung angka!")
else:
    b = input("Kata 2: ")
    
    if not b.isalpha():
        print("Input tidak boleh mengandung angka!")
    else:
        if is_anagram(a, b):
            print("Anagram")
        else:
            print("Bukan Anagram")
