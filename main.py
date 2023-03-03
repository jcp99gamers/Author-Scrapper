import requests
from bs4 import BeautifulSoup
filename = "author_prisha_chawla.md"

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
    date = date_element.get('datetime')
    # Extract the excerpt
    excerpt_element = article.find('div', {'class': 'excerpt'})
    excerpt = excerpt_element.text.strip()
    # Find the image source of the article
    image_src = article.find('span', {'class': 'img'})['data-bgsrc']
    # Print the extracted information
    print('Title:', title)
    print('Category:', category)
    print('Date:', date)
    print('Image Source:', image_src)
    print('Content/Excerpt:', excerpt)
    print('Read More Link:', read_more_link)
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
        date = article.find('time', {'class': 'post-date'})['datetime']
        # Find the category of the article
        category = article.find('a', {'class': 'category term-color-1'}).text.strip()
        # Find the image source of the article
        image_src = article.find('span', {'class': 'img'})['data-bgsrc']    
        #  Find the read more link of the article
        read_more_link = article.find('a', {'class': 'read-more-link read-more-btn ts-button ts-button-alt'})['href']    
        # Get the excerpt of the article
        excerpt = article.find('div', {'class': 'excerpt'}).text.strip()    
        # Print the extracted information
        print('Title:', title)
        print('Category:', category)
        print('Date:', date)
        print('Image Source:', image_src)
        print('Content/Excerpt:', excerpt)
        print('Read More Link:', read_more_link)
        print()
    except:
        break