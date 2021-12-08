def fibo(stop, arr=[], fib=0, item=1):
    arr.append(fib)
    fib += item
    item = fib - item
    if fib < stop:
        return fibo(stop, arr, fib, item)
    return arr


stop = 10

print(fibo(stop))