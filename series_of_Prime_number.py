# the series of prime number 
limit = int(input("Enter the Limit  : = ")) # 100 

for j in range(1 ,limit + 1): # 5
    cnt = 0 # 0
    for i in range(2 , j ):# 3 
        if j % i == 0 : # 5 % 4 == 0 
            cnt += 1 
            break
    if cnt == 0 :
        print(j , end = " , ")
   