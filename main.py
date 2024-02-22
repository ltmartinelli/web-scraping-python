from bs4 import BeautifulSoup
import requests
import pandas as pd

'''Specify URL, GET page with requests and use BeautifulSoup to parse it'''

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

'''Find the Table and Headers, you can use the class name to do it, too'''

table = soup.find_all('table')[1]
headers = table.find_all('th')

'''
Loop through headers lists, get only the text and strip it to remove line break
Add them as columns to Data Frame with Pandas
'''

world_table_headers = [header.text.strip() for header in headers]
data_frame = pd.DataFrame(columns=world_table_headers)

'''Find the Table Rows in the table'''

column_data = table.find_all('tr')

'''
Loop through the rows, extract the Table Data stripped text into a list
Check the Data Frame length in each loop, and use it to insert the data
'''

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(data_frame)
    data_frame.loc[length] = individual_row_data

'''Export DataFrame as CSV'''

data_frame.to_csv(r'.\companies.csv', index=False)
