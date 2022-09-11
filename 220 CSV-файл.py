# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
# Напишите функцию read_csv для чтения данных из этого файла.
# Она должна возвращать список словарей, интерпретируя первую строку как имена ключей,
# а каждую последующую строку как значения этих ключей.
#
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна содержать реализованную функцию read_csv.

def read_csv():
    needWriteKeys = True
    keys = []
    result = []

    with open('data.csv') as file:
        for line in file.readlines():
            if needWriteKeys:
                keys = line.strip().split(',')
                needWriteKeys = False
            else:
                result.append(dict(zip(keys, line.strip().split(','))))
    return result
