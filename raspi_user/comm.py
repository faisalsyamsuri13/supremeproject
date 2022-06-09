#for Raspberry Pi Users, put this file with the control program for being executed from the Bash command prompt
#using key generator for identifying and calling the row to be generated in QR Code

#communication module being used for posting data
import csv
import requests
import random
import socket
import keygen
import qrgen

#accessing txt file
#text = open('temp.txt', 'r')
#list = text.readlines()

#accessing csv file
file = open("color.csv", "r")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
lines = len(rows)

#server setting
ip_address = socket.gethostbyname(socket.gethostname())
api_url = 'http://{}/supremeproject/post-sql-data.php'.format(ip_address)
api_key_value = 'tPmAT5Ab3j7F9'

#key = keygen.key

#array iteration from 'text' (txt file)
sensor = "AS7341"
location = "Electronics Lab"
value1 = rows[lines-1][1]
value2 = rows[lines-1][2]
value3 = rows[lines-1][3]
value4 = rows[lines-1][4]
value5 = rows[lines-1][5]
value6 = rows[lines-1][6]
value7 = rows[lines-1][7]
value8 = rows[lines-1][8]
value9 = rows[lines-1][9]
value10 = rows[lines-1][10]
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
    except:
        print("Unable to connect and post the data to the server, please check the server configuration!")

#direct posting via import
#try:
#   response = requests.post(server_name, data = myobj)
#   print(response.text)
#except:
#   print("Cannot connect and post the data to the server, please check the server configuration!")
