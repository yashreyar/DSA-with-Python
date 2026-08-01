'''
Input = 13
Output = "1101"
'''

def convert_to_binary(num):
    result = ""
    
    while num > 0:
        remainder = num % 2
        if remainder == 1:
            result = "1" + result
            
        else:
            result = "0" + result
        
        num = num // 2
        
    return result

print(convert_to_binary(num=13))