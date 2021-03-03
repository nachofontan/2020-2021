new_list = [0,1]
x = 0
y = 1
n = 11
for i in range(1, n - 1):
    sum = x + y
    x = y
    y = sum
    new_list.append(sum)
print(new_list)