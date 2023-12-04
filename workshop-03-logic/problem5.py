##### sets range of numbers to test if divisible by
max=20
if(max%2==0):
    min = int(max/2+1)
else:
    min = int((max+1)/2)


pd = max * (max-1)
val=pd
ans = 1

### Tests possible numbers
while (ans==1):
    for i in range(min,max-1,1):
        if (i==max-2 and val % i == 0):
            ans = 2
        elif(val % i != 0):
            val+=pd
            break
                


print(val) 





