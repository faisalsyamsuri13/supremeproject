#for Raspberry Pi Users, put this file with the control program for being executed from the Bash command prompt
#using key generator for identifying and calling the row to be generated in QR Code

#communication module being used for posting data
import requests
import random
#import keygen

#accessing txt file
text = open('temp.txt', 'r')
list = text.readlines()

#server setting
server_name = 'http://ip_address/supremeprojectv2/post-sql-data.php'
api_key_value = 'tPmAT5Ab3j7F9'

#key = keygen.key

#array iteration from 'text' (txt file)
sensor = "AS7341"
location = "Electronics Lab"
value1 = list[0]
value2 = list[1]
value3 = list[2]
value4 = list[3]
value5 = list[4]
value6 = list[5]
value7 = list[6]
value8 = list[7]
value9 = list[8]
value10 = list[9]
#keygen = key
#link = '<a href="preview.php?id={}>Preview</a>"'.format(keygen)

#key-value pair for accessing the variable in the PHP server file
myobj = {'api_key':api_key_value,
         'sensor':sensor,
         'location':location,
         'value1':value1,
         'value2':value2,'value3':value3,'value4':value4,'value5':value5,'value6':value6,'value7':value7,'value8':value8,'value9':value9,'value10':value10}

#posting to the server and retrieving the response
response = requests.post(server_name, data = myobj)
print(response.text)
