def count_word_frequency_in_sentence(sentence):
    
    words = sentence.lower().split()
    word_count = {}
    
    result = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
            
        else:
            word_count[word] = 1
            
    return word_count

print(count_word_frequency_in_sentence("The quick brown fox jumps over the lazy fox"))