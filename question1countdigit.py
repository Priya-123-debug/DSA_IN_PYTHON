def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

n = 5438
print(count_digits(n))