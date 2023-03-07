import os
import time
import shutil
import datetime
import requests
import pathlib as pb
from bs4 import BeautifulSoup

path = pb.Path(__file__).parent.resolve().as_posix() #Used for Python Files
drive, rest = os.path.splitdrive(path)

filename = "/README.md"

def timeConverter(timestamp_str):
    timestamp = datetime.datetime.fromisoformat(timestamp_str)
    formatted_timestamp = timestamp.strftime('%d-%m-%Y %H:%M:%S IST') # %Z
    return formatted_timestamp
"""
try:
    with open(path+filename, encoding="cp1252") as f:
        fTitle = f.readline()
except:
    f = open(path+filename, "r")
    fTitle = f.readline()
finally:
    print(fTitle)
    pass
"""

f = open(path+filename, "w")
f.write("# Author-Prisha-Chawla"+"\n")

#
URL = r'https://asianatimes.com/author/prisha-chawla/'
# Make a request to the webpage
response = requests.get(URL)
# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the article containers on the page
article_containers = soup.find_all('article', {'class': 'l-post grid-post grid-base-post'})
# Loop through each article container and extract the desired data
for article in article_containers:
    # Extract the title and link
    title_element = article.find('a', {'class': 'image-link'})
    title = title_element.get('title')
    read_more_link = title_element.get('href')
    # Extract the category and date
    category_element = article.find('a', {'class': 'category'})
    category = category_element.text.strip()
    date_element = article.find('time', {'class': 'post-date'})
    datez = date_element.get('datetime')
    date = timeConverter(datez)
    # Extract the excerpt
    excerpt_element = article.find('div', {'class': 'excerpt'})
    excerpt = excerpt_element.text.strip()
    # Find the image source of the article
    image_src = article.find('span', {'class': 'img'})['data-bgsrc']
    # Print the extracted information
    f = open(path+filename, "a")
    f.write("##\t"+title+"\n")
    print('Title:', title)
    f.write("######\t"+category+"\n")
    print('Category:', category)
    f.write("######\t"+date+"\n")
    print('Date:', date)
    f.write("!["+title+"]("+image_src+")\n")
    print('Image Source:', image_src)
    f.write("###\t"+excerpt+"\n")
    print('Content/Excerpt:', excerpt)
    f.write("[Read More Link]("+read_more_link+")\n")
    print('Read More Link:', read_more_link)
    f.write("\n\n")
    print()

#HAD TO MAKE A DIFFERENT METHOD CAUSE THIS WEBPAGE ISNT CODED PROPERLY
URL = r"https://www.inpactimes.com/author/prisha-chawla/"# URL of the page to be scraped
# Send a GET request to the URL
response = requests.get(URL)
# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the article elements on the page
articles = soup.find_all('article', {'class': 'l-post grid-post grid-base-post'})
# Loop through each article and extract the relevant information
for article in articles:
    try:
        # Get the title of the article
        title = article.find('h2', {'class': 'is-title post-title'}).text.strip()    
        # Get the date of the article
        datez = article.find('time', {'class': 'post-date'})['datetime']
        date = timeConverter(datez)
        # Find the category of the article
        category = article.find('a', {'class': 'category term-color-1'}).text.strip()
        # Find the image source of the article
        image_src = article.find('span', {'class': 'img'})['data-bgsrc']    
        #  Find the read more link of the article
        read_more_link = article.find('a', {'class': 'read-more-link read-more-btn ts-button ts-button-alt'})['href']    
        # Get the excerpt of the article
        excerpt = article.find('div', {'class': 'excerpt'}).text.strip()    
        # Print the extracted information
        f = open(path+filename, "a")
        f.write("##\t"+title+"\n")
        print('Title:', title)
        f.write("######\t"+category+"\n")
        print('Category:', category)
        f.write("######\t"+date+"\n")
        print('Date:', date)
        f.write("!["+title+"]("+image_src+")\n")
        print('Image Source:', image_src)
        f.write("###\t"+excerpt+"\n")
        print('Content/Excerpt:', excerpt)
        f.write("[Read More Link]("+read_more_link+")\n")
        print('Read More Link:', read_more_link)
        f.write("\n\n")
        print()
    except:
        break

f.close()

'''
#UNCOMMENT IF RUNNING ON WINDOWS
os.chdir(path)  # Change the current working directory to the directory of the 
# Get the parent directory of the current working directory
parent_dir = os.path.dirname(os.getcwd())
# Change the working directory to the parent directory
os.chdir(parent_dir)
# os.system("cd "+drive)
# os.system("cd "+path)
time.sleep(5)
folder_name = '__pycache__'
try:
    shutil.rmtree(folder_name)
    os.rmdir(folder_name)
    print(f"{folder_name} folder deleted successfully.")
except OSError as e:
    print(f"Error: {folder_name} folder could not be deleted. {e}")
os.system("git status")
os.system("git add .") # os.system("git add .\README.md") 
now = datetime.datetime.now() # Get the current date and time
formatted_date = now.strftime("%B %dth %Y %I:%M%p") # Convert to "March 7th 2023 12:38Pm" format
commit = 'git commit -m "'+formatted_date +' Update."'
os.system(commit)
os.system("git push -u origin main")
'''

print("\nDone!")

















"""
# </,JCP99GAM3Rs...>
"""