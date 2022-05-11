#for Raspberry Pi Users, put this file with the control program for being executed from the Bash command prompt
#using key generator for identifying and calling the row to be generated in QR Code

#communication module being used for posting data
import requests
import random
#import keygen

#accessing txt file
#text = open('temp.txt', 'r')
#list = text.readlines()

#server setting
server_name = 'http://192.168.0.112/supremeproject/post-sql-data.php'
api_key_value = 'tPmAT5Ab3j7F9'

#key = keygen.key
n1 = "1234"
n2 = "0123456789"

#array iteration from 'text' (txt file)
sensor = "AS7341"
location = "Electronics Lab"
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
#keygen = key
#link = '<a href="preview.php?id={}>Preview</a>"'.format(keygen)
#value3 = list[12] + "".join('{}'.format(i) + '">Preview</a>')

#key-value pair for accessing the variable in the PHP server file
myobj = {'api_key':api_key_value,
         'sensor':sensor,
         'location':location,
         'value1':value1,
         'value2':value2,
         'value3':value3,
         'value4':value4,
         'value5':value5,
         'value6':value6,
         'value7':value7,
         'value8':value8,
         'value9':value9,
         'value10':value10
        }

#posting to the server and retrieving the response
response = requests.post(server_name, data = myobj)
print(response.text)
