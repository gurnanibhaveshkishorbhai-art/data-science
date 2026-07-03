price = [25000,30000,45000,50000,65000]

target = 50000

ans = -1

for i in range(len(price)):
    if price[i] >= target:
        ans = price[i]
        break

print(ans)