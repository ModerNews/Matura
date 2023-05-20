def fibonacci_rec(n, arr=[0, 1]):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        if len(arr) >= n:
            return arr
        else:
            arr.append(arr[-1] + arr[-2])
            fibonacci_rec(n, arr)
    return arr


def fibonacci_iter(n):
    if n in (0, 1):
        return n
    else:
        arr = [0, 1]
        for i in range(2, n):
            arr.append(arr[-1] + arr[-2])
        return arr
