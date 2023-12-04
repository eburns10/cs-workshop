### Stores number
num = 0
### Tests if divisible
for i in range(0,1000,1):
    if (i%3==0 or i%5==0):
        num += i

print(num)