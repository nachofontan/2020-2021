def fibon(n):
    new_list = [0,1]
    x = 0
    y = 1
    for i in range(1, n - 1):
        sum = x + y
        x = y
        y = sum
        new_list.append(sum)
    return new_list
print("5 Fibonacci terms ", fibon(5) )
print("10 Fibonacci terms ", fibon(10) )
print("15 Fibonacci terms ", fibon(15) )
