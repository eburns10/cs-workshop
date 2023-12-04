
high = 0
num=6857

if(num%2==0):
    for i in range(2,int((num/2)+1),1):
        if(num%i==0 and i%2==1):
            prime=1
            for j in range (3,int((num/i+1)/2),2):
                if(int(num/i)%j==0):
                    prime=2
            if(prime==1):
                high=int(num/i)
                break  
else:
    for i in range(3,int((num+1)/2),2):
        print(i)
        if(num%i==0):
            print("found")
            prime=1
            for j in range (3,int((num/i+1)/2),2):
                if(int(num/i)%j==0):
                    prime=2
                    break
            if(prime==1):
                high=int(num/i)
                break       
        

print(high)