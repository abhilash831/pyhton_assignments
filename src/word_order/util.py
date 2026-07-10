def get_word_order(words):
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    distinct_count = str(len(word_counts))
    frequencies = " ".join(str(count) for count in word_counts.values())
    
    return f"{distinct_count}\n{frequencies}"