import os,sys, pdb
from bs4 import BeautifulSoup # Checkout Scrapy library for more advanced WebScrapping
import requests
import pandas as pd
from pathlib import Path



def explore(res):            
    
    soup = BeautifulSoup(res.text,'html.parser')  # Convert html text into usful soup object
    news_items = soup.find_all(class_ = 'athing') # Find all the news in the web page

    for item in news_items:  # Loop through each news item and extract relevant information
        try:           
            title_line = item.find(class_= 'titleline')

            title = title_line.find('a').text
            link = title_line.find('a')['href']
            score = item.find_next('tr').find(class_ = 'score')
            

            if score == None:
                score = 0
            else:
                score = extract_int_until_non_int(score.text)

            news_data.append({'title': title,'link': link, 'score': score })

        except:
            pass


# predefined function by help of ChatGPT to get int value out of set of text '54852 D090CA3' ==> '54852'
def extract_int_until_non_int(input_string):
    num_str = ""
    for char in input_string:
        if char.isdigit():
            num_str += char
        else:
            break
    if num_str:
        return int(num_str)
    else:
        return None


# change cwd for desired path as in VScode's cwd in desktop
current_path = Path(sys.argv[0]).parent
os.chdir(current_path) 

news_data = [] # Store site data

for page in range(1,10):
    res = requests.get(f'https://news.ycombinator.com/news?p={page}') 
    explore(res)
    print(f'done page number: {page}')

news_data.sort(key= lambda x: x['score'], reverse= True) # Sorting the list of news based on highest voting rate

df = pd.DataFrame(news_data)
df.to_excel(current_path.joinpath('news_data.xlsx'), index= False) # Cast results into an excel file
