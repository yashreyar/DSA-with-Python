def gcd(n, m):
    while m > 0:
        remainder = n % m       # 1. Get the leftover
        n = m                   # 2. The smaller number becomes the new big number
        m = remainder           # 3. The leftover becomes the new small number
    return n 

print(gcd(48, 18))