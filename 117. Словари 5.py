# Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам,
# складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях.
# Результирующий словарь необходимо присвоить переменной result.
#
# Примечание. Выводить содержимое словаря result не нужно.

dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

for key, value in dict2.items():
    dict1[key] = dict1.setdefault(key, 0) + value
result = dict1.copy()
