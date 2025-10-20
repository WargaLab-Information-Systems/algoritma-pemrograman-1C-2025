n = int(input("masukkan angka:  "))

prima=[]
for num in range(1,n+1):
    if num > 1 :
        for i in range(2,num) :
            if num%i ==0:
                break
            
        else:
            prima.append(num)
print("bilangan prima dari 1 sampai",n,"adalah:",prima)                  



