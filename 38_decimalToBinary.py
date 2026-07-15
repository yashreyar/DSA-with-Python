def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    is_negative = n < 0
    n = abs(n)
    
    result = ""
    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2
        
    if is_negative:
        result = "-" + result
        
    return result

print(decimal_to_binary(5))