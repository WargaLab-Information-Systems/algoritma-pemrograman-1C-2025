# # # def sapa(): 
# # #     print ("Haloo Dunia")

# # def tambah (a, b):
# #     c = a + b 

# #     print("Hasil Penjumlahan :", c)
# #     print ("coba")
# #     return c

# # tambah (3,4)
# tambah = lambda x, y, z: x + y + z 
# print (tambah(10, 2, 5))

# print((lambda k:k))

def faktorial(n):
    if n == 1:
        return 1 
    else:
        return n + faktorial(n-1)
    
    print (faktorial(3))




    