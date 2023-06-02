from bs4 import BeautifulSoup
import requests
# from os import system

# todo: chacking the internet connection function --->
def check_Internet_connection(url='http://www.google.com/', timeout=3):
    try:
        r = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        return False

if(check_Internet_connection() == 0):
    print(" There is no internet Connection \n  Check your internet Connection ...")
    # this is for keeping the program open---->
    k = input("\npress enter key to exit ----- ")
    # this is for stoping the program from running
    sys.exit()
# todo: chacking the internet connection function --->

# start coding -----------------------
k = input('    be sure that you have a suitable internet connection Then press (Enter) key to start ...')
# print('\n', 'please waite ...')

# ! loading_shape fuction --->
import threading
import time
loop_end = 1

def loading():
    import time
    print('')
    while loop_end == 1:
        loading_list = ['--', '\\\\', '||', '//']
        for i in range(len(loading_list)):
            print('  -> Loading ', loading_list[i], end='\r')
            time.sleep(0.15)
    if loop_end == 0:
        print(end='\r')
        print("  -> Loading Compleated .")

    return()
loading = threading.Thread(name='loading', target=loading).start()
# ! loading_shape fuction --->

# creating a response object site information
response = requests.get('https://www.worldometers.info/coronavirus/')

# finding the response text
website_text = response.text

# defining the website_text to the BeautifulSoup
soup = BeautifulSoup(website_text, 'html.parser')

# prettify makes the code more comefortable for reading and give it a good look
# print(soup.prettify())

# output of find_all function is a list
# finding all the tables in the website_text
table_list = soup.find_all('table', attrs={'id':'main_table_countries_today'})

# finding that how many tables are there in the webpage match to our id
# print('tables match to our id :', len(table_list))

# defining our table that we found
table = table_list[0]

# finding the tbody of the table
tbody_list = table.find_all('tbody')
tbody = tbody_list[0]

# finding the trs of the tbody
tr_list = tbody.find_all('tr')

# finding the Iran str in web
for i in range(len(tr_list)):
    country_td = tr_list[i].find_all('td')
    country_td_text = country_td[1].text
    if country_td_text == 'Iran':
        # save the iran tds
        iran_tds = country_td
        break

# difining the (iran_information) list and put the (iran_tds) in it
iran_information = []

for i in iran_tds:
    texts = i.text
    iran_information += [texts]

# ! this is for finishing the loading_shape --->
loop_end = 0
time.sleep(0.5)

print('\n', 'Country Name :', iran_information[1], '\n')
print('Iran ranking in the world :', iran_information[0], '\n')
print('Population :', iran_information[14], '\n')
print('Total cases :', iran_information[2], '\n')
print('New cases :', iran_information[3], '\n')
print('Total deaths :', iran_information[4], '\n')
print('-> New deaths :', iran_information[5], '\n')
print('Total recovered :', iran_information[6], '\n')
print('New Recovered :', iran_information[7], '\n')

k = input('press Enter key to exit .........')