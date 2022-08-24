# Список data содержит слова на русском языке.
# Напишите программу его сортировки по возрастанию длины слов, а затем в лексикографическом порядке.
# Отсортированные слова следует вывести на одной строке, разделив символом пробела.

data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

sorted_data = sorted(data)

new_data = sorted(sorted_data, key=lambda word: len(word))

print(*new_data)
