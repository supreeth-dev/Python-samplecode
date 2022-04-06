print("Hello World")
num = [10, 5 , 8 , 6, 1]
for i in range(0,len(num)):
    print(i)
    min_idx = i
    
    for j in range(i+1,len(num)):
        if(num[j] < num[min_idx]):
            min_idx = j
    
    num[min_idx],num[i] = num[i],num[min_idx]

print(num)
            
