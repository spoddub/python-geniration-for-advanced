# Функция ignore_command() принимает на вход один строковый аргумент command – команда,
# которую нужно проверить, и возвращает значение True,
# если в команде содержится подстрока из списка ignore и False – если нет.
# Перепишите функцию ignore_command(),
# чтобы она использовала встроенные функции all()/any() сохранив при этом ее функционал.

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: x in command, ignore))
