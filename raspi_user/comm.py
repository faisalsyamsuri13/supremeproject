#for Raspberry Pi Users

import requests

#accessing txt file
text = open('temp.txt', 'r')
list = text.readlines()

#increment, need to be modified
i = 0
i = i + 1

#server setting
url = 'http://ip_address/supremeproject/post-sql-data.php'
api_key_value = 'tPmAT5Ab3j7F9'

#array iteration from 'text' (txt file)
sensor = list[0]
location = list[1]
value1 = list[2]
value2 = list[3]
value3 = list[4] + "".join('{}'.format(i) + '">Preview</a>')

#key-value pair for accessing the variable in the PHP server file
myobj = {'api_key':api_key_value,'sensor':sensor,'location':location, 'value1':value1, 'value2':value2, 'value3':value3}

#posting to the server and retrieving the response
response = requests.post(url, data = myobj)
print(response.text)
