### Stores numbers
v1 = 0
v2 = 0

#### Adds squares/values onto previous amount
for i in range(0,101,1):
    v1 += i**2
    v2 += i

v2 = v2**2
delta = v2 - v1
print(delta)
