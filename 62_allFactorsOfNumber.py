'''
Print all factors of a number

Input = 10
Output = [1,2,5,10]
'''

def are_factors(n):
    lst = []
    if n <= 0:
        return []
    for i in range(1, (n//2) + 1):
        if n % i == 0:
            lst.append(i)
    lst.append(n)    
    return lst

print(are_factors(n=1))

'''
def are_factors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst

print(are_factors(n=20))
'''