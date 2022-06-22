import csv
from csv import writer
import random
import datetime

n1 = '1234'
n2 = '0123456789'

str_date = str(datetime.datetime.now())
cur_date = str_date[0:19]
value1 = "".join(random.sample(n1, 1) + random.sample(n2, 4))
value2 = "".join(random.sample(n1, 1) + random.sample(n2, 3))
value3 = "".join(random.sample(n1, 1) + random.sample(n2, 4))
value4 = "".join(random.sample(n1, 1) + random.sample(n2, 4))
value5 = "".join(random.sample(n1, 1) + random.sample(n2, 3))
value6 = "".join(random.sample(n1, 1) + random.sample(n2, 3))
value7 = "".join(random.sample(n1, 1) + random.sample(n2, 4))
value8 = "".join(random.sample(n1, 1) + random.sample(n2, 3))
value9 = "".join(random.sample(n1, 1) + random.sample(n2, 3))
value10 = "".join(random.sample(n1, 1) + random.sample(n2, 4))

list_data = [cur_date, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, 'RESULT']

with open('color.csv', 'a', newline='') as f:
    writer_object = writer(f)
    writer_object.writerow(list_data)
    f.close()
