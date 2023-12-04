mySum = 0
for i in range(0, 1001, 1):
    if i % 2 == 0:
        mySum += 1
    elif i% 7 == 0:
        print('this is divisible by 7')
    else: 
        print("none of the above")

print(mySum)