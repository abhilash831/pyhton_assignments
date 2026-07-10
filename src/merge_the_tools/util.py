def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = ""
        for char in t:
            if char not in u:
                u += char
        print(u)