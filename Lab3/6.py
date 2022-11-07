arr = [1,2,3,4,4,6]
val = 0
for i in range(len(arr)):
    val += arr[-i-1]*10**i
print(val)