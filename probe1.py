def func(number):
        answer = True
        if number % 19 == 0 or number % 13 == 0:
                answer = True
        else:
                answer = False

        return answer




print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))