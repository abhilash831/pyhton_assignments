def mutate_string(string, position, character):
    list1 = list(string)
    
    for i, j in enumerate(list1):
        if i == position:
            list1[i] = character
            break
            
    return "".join(list1)