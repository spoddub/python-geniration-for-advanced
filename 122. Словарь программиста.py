# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык.
# Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу.
# Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.
#
# Формат входных данных
# В первой строке задано одно целое число n — количество слов в словаре.
# В следующих n строках записаны слова и их определения, разделенные двоеточием и символом пробела.
# В следующей строке записано целое число m — количество поисковых слов, чье определение нужно вывести.
# В следующих m строках записаны сами слова, по одному на строке.
#
# Формат выходных данных
# Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение.
# Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.

mydict = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    mydict[key.lower()] = value

for _ in range(int(input())):
    print(mydict.get(input().lower(), 'Не найдено'))
