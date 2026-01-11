# Prime number program in Python
limit = int(input("Enter The Limit : "))
# range will start from 2 to < n
for i in range(1,limit+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt+=1
            break
    if cnt == 0:
        print(i,end = " , ") 
# end is a seperator to print output sepearted by comma
    

