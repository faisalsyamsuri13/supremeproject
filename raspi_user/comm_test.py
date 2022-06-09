#for Raspberry Pi Users, put this file with the control program for being executed from the Bash command prompt
#using key generator for identifying and calling the row to be generated in QR Code

#communication module being used for posting data
import requests
import random
import socket
import keygen
import qrgen

#accessing txt file
#text = open('temp.txt', 'r')
#list = text.readlines()

#server setting
ip_address = socket.gethostbyname(socket.gethostname())
api_url = 'http://{}/supremeproject/post-sql-data.php'.format(ip_address)
api_key_value = 'tPmAT5Ab3j7F9'
#head = {"Content-Type":"application/x-www-form-urlencoded"}

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
pub_key = keygen.key
#link = '<a href="preview.php?id={}>Preview</a>"'.format(keygen)

#key-value pair for accessing the variable in the PHP server file

my_data = {'api_key':api_key_value,
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
         'value10':value10,
         'pub_key':pub_key
        }

#posting to the server and retrieving the response
#posting by function
def response():
    try:
        post_data = requests.post(api_url, data = my_data)
        print(post_data.text)
        qrgen.generate()
    except Exception as e:
        print("Cannot connect and post the data to the server, please check the server configuration! Error: {}".format(e))
#direct posting via import
#try:
#   response = requests.post(server_name, data = myobj)
#   print(response.text)
#except:
#   print("Cannot connect and post the data to the server, please check the server configuration!")
