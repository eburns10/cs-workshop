
### Creates numbers that store fibonacci numbers
i=1 
j=2
k=3
term=4
exp =1000

#### Tests numbers
while(k < 10**(exp-1) ):
    i = j
    j= k
    k = i + j
    term += 1

print(term)