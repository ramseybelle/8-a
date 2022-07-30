def count_letters(s: object) -> object:
    d = {}
    for ch in s:
        ch = ch.upper()
        if 'A' <= ch <= 'Z':
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
    return d


# Testing the function here. ignore/remove the code below if not required
print(count_letters("AaBb"))
