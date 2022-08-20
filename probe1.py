func = lambda word: str(word).lower().endswith('a') and str(word).lower().startswith('a')


print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))