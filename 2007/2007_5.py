def is_prime(number: int):
    return number != 1 and not any(number % divider == 0 for divider in range(2, number//2 + 1))

def is_super_B_prime(number: int):
    cipher_sum = 0
    for cipher in str(number):
        cipher_sum += int(cipher)

    cipher_sum_b = 0
    for cipher in str(bin(number))[2:]:
        cipher_sum_b += int(cipher)

    return is_prime(number) and is_prime(cipher_sum) and is_prime(cipher_sum_b)

print('a)')
print(len([n for n in range(2, 1001) if is_super_B_prime(n)]))
print(len([n for n in range(100, 10001) if is_super_B_prime(n)]))
temp = [n for n in range(1000, 100001) if is_super_B_prime(n)]
print(len(temp))
print('b) 1')
k = 0
for i in range(100, 10001):
    cipher_sum = 0
    for cipher in str(i):
        cipher_sum += int(cipher)
    if is_prime(cipher_sum):
        k += 1
print(k)
print('b) 2')
print(is_prime(sum(temp)))