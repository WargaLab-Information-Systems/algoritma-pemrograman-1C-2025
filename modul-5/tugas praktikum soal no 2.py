def cek_anagram(kata1, kata2):
    return sorted(kata1) == sorted(kata2)

print("=== PROGRAM CEK ANAGRAM ===")

while True:
    print("\n--- CEK ANAGRAM ---")
    kata1 = input("kata pertama: ")
    kata2 = input("kata kedua: ")
    
    if cek_anagram(kata1, kata2):
        print(f" '{kata1}' dan '{kata2}' ADALAH ANAGRAM!")
    else:
        print(f" '{kata1}' dan '{kata2}' BUKAN ANAGRAM!")
    
    lanjut = input("cek lagi? (y/n): ").lower()
    if lanjut != 'y':
        print("yawdah sih")
        break