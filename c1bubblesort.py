num = [7, 3, 9, 1, 5]

for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j] > num[j+1]:
            t = num[j]
            num[j] = num[j+1]
            num[j+1] = t

print(num)