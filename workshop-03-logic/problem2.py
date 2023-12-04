#### Stores fibonacci numbers
total=2
i = 1
j = 2
k = 3

### Tests numbers
while(k < 4e6):
    if(k % 2 == 0):
        total += k
    i = j
    j = k
    k= i+j

print(total)
