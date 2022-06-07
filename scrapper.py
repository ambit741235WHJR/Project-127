# Importing necessary Libraries and Modules
import requests, time, pandas as pd
from bs4 import BeautifulSoup

# Defining the START_URL
START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

# Creating a function to get the data from the webpage
def get_data(url):
    # Getting the webpage
    response = requests.get(url)

    # Creating a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding the table
    table = soup.find('table')

    # Finding the rows
    rows = table.find_all('tr')

    # Creating a list to store the data
    data = []
    
    # Looping through the rows
    for row in rows:
        # Finding the columns
        columns = row.find_all('td')
        # Creating a list to store the data
        row_data = []
        # Appending the data to the list
        row_data.append([i.text.rstrip() for i in columns])
        # Appending the list to the data list
        data.append(row_data)
    
    # Creating headers
    headers = ['Name', 'Distance', 'Mass', 'Radius', 'Luminosity']

    # Creating variables
    name = []
    distance = []
    mass = []
    radius = []
    luminosity = []

    # Looping through the data
    for i in range(1, len(data)):
        # Appending the data to the variables
        name.append(data[i][0][1])
        distance.append(data[i][0][3])
        mass.append(data[i][0][5])
        radius.append(data[i][0][6])
        luminosity.append(data[i][0][7])
    
    # Creating a dataframe
    df = pd.DataFrame(list(zip(name, distance, mass, radius, luminosity)), columns=headers)
    
    # Returning the dataframe to a csv file
    df.to_csv('data.csv')

get_data(START_URL)