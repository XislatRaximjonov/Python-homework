def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testlar
print(is_prime(4))  # False
print(is_prime(7))  # True


def digit_sum(k):
    return sum(int(d) for d in str(k))

# Testlar
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7


def powers_of_two(n):
    power = 2
    result = []
    while power <= n:
        result.append(power)
        power *= 2
    return result

# Test
print(powers_of_two(10))  # [2, 4, 8]

# Chop etish formati bo‘yicha
print(*powers_of_two(10))  # 2 4 8
