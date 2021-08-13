import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import numpy as np

cats_wiki = 'https://en.wikipedia.org/wiki/List_of_cat_breeds'
page = requests.get(cats_wiki)

soup = BeautifulSoup(page.text, 'html.parser')
'''
x = ''

for body_child in soup.body.children:
    if isinstance(body_child, NavigableString):
        continue
    if isinstance(body_child, Tag):
        x = x + body_child.name
        
print(x)
'''
cat_table = soup.find('table', class_='wikitable')

breed = []
country = []
origin = []
body_type = []
coat_length = []
pattern = []
images = []

for row in cat_table.find('tbody').find_all('tr'):
    breed_info = row.find_all('td')
    breed_name = row.find('th')
    
    if len(breed_info) == 6:
        breed.append(breed_name.find(text = True))
        country.append(breed_info[0].find(text = True))
        origin.append(breed_info[1].find(text = True))
        body_type.append(breed_info[2].find(text = True))
        coat_length.append(breed_info[3].find(text = True))
        pattern.append(breed_info[4].find(text = True))
        
        if breed_info[5].find('img'):
            images.append(breed_info[5].find('img').get('src'))
        else:
            images.append('No Image')
            
cat_breed_df = pd.DataFrame(
    {'Breed': breed,
     'Country': country,
     'Origin': origin,
     'Body Type': body_type,
     'Coat Length': coat_length,
     'Pattern': pattern,
     'Images': images
    })

cat_breed_df.set_index('Breed', inplace=True)
pd.set_option('display.max_columns', None)
print(cat_breed_df['Body Type'].head())

def get_bodyType(item):
    item = str(item)
    if '\n' in item:
        return item[:item.find('\n')]
    else:
        return item

#(cat_breed_df.type())
print('\n')
print(cat_breed_df)
cat_breed_df = cat_breed_df.applymap(get_bodyType)
print(cat_breed_df['Body Type'].head())
print('\n')
print(cat_breed_df)