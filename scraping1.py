from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import csv
#creating a variable for the url and storing the website link
START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
#using requests module to exchange requests on the web .get() is the method used to request data from the server
wiki = requests.get(START_URL)
#printing the data requested
print(wiki)
#extract the source using bs4 (browser page is the address of the webpage) using the function that is designed to analyse this designated webpage 
soup = BeautifulSoup(wiki.text, "html.parser")
#finding out all elements with the tag "table"
star_table = soup.find_all('table')
#printing number of items in table
print(len(star_table))
#creating an empty list to store the stars data
temp_list= []
#getting all the tr tags from the table
table_rows = star_table[4].find_all('tr')
#using a for loop to take out all the td tags and needing all the text
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)

#creating empty list to store headers data
Star_names = []
Distance =[]
Mass = []
Radius =[]
#looping through the row list to get the data and append it to the lists
for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
#creating a dataframe from the list created in the previous steps
df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df)
#creating a csv file from the list
df.to_csv('dwarfs.csv')