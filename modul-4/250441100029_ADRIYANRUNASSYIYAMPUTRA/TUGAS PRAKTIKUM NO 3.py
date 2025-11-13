n=int(input("input jumlah pola baris bilangan "))
lebar=n*2
spasi=" "
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    rumus_spasi=lebar-(i*2)
    print(rumus_spasi*spasi,end="")
    for z in range (j,0,-1):
        print(z,end="")
    print()