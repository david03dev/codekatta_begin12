#Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a
import math
#import numpy as np
input_string = input()
a = list(input_string.split())

A = int(a[0])
B = int(a[1])
C = int(a[2])

res = 0
res = -(B - math.sqrt(B*B - (4 * A *C )))
res = res /(2* A)

X = format(round(res / 2,2),".2f")

res = -(B + math.sqrt(B*B - 4 * A *C ))
res = res /(2* A)

Y = format(round(res / 2,2),".2f")

print(X)
print(Y)
