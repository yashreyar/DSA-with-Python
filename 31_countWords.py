def count_words(s):
    words = s.lower().split()
    word_count = {}
    
    for word in words:
        
        if word in word_count:
            word_count[word] += 1
            
        else:
            word_count[word] = 1
            
    return word_count

print(count_words("Hello Word word"))