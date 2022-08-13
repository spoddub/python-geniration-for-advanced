from decimal import *
num = Decimal(input())
answer = num.exp() + num.ln() + num.log10() + num.sqrt()
print(answer)