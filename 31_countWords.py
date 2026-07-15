def count_words(s):
    words = s.lower().split()
    count = 0
    
    for word in words:
        count += 1
    return count

print(count_words("Hello Word word"))