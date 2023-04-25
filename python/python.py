
x = 1
 
y = 1

while x < 5:
    if x % 2 == 0:
        y *= x
    else:
        y += x
    x += 1

print(y, x)