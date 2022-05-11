import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol= "[]{}<>#()*._-;"

ans = lower_case + upper_case + number + symbol
length = 10
key = "".join(random.sample(ans,length))
