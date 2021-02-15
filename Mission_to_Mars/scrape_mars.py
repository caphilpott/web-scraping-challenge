# Dependencies - required modules
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import lxml.html as lh
import time

#def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
#    executable_path = {'executable_path': ChromeDriverManager().install()}
#    return Browser("chrome", **executable_path, headless=False)

#Generate the scrape function which will generate all the requested data and store it in a dictionary
def scrape():
    #browser = init_browser()
    
    # create mars_data dict that we can insert into mongo
    mars_data = {}
    
    # NASA Mars News
    
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?&blank_scope=Latest'
    time.sleep(1)
    
    # Retrieve page with the requests module  - #http get request to the url
    response = requests.get(url)
    time.sleep(1)
    
    # Create BeautifulSoup object; parse with 'lxml
    soup = BeautifulSoup(response.text, 'lxml')
    time.sleep(1)
    
    # Retrieve the title and paragraph for the article - note, results are returned as an iterable list
    res = soup.find('div', class_='image_and_description_container')
    time.sleep(1)
    
    # scrape the article title and article paragraph
    news_title = res.find_next(class_="content_title").text
    news_p = res.find(class_="rollover_description_inner").text

    # add our news to the mars dictionary
    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p
    
    # JPL Mars Space Images - Featured Image
    
    # Setup splinter 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Link up to the jet propulsion labs nasa web site
    url = 'https://www.jpl.nasa.gov/'
    browser.visit(url)
    time.sleep(10)
    
    #Find and click on the images button
    #browser.links.find_by_partial_text('Images').click()
    browser.links.find_by_partial_text('Images').click()
    time.sleep(8)

    #Select Mars filter
    browser.find_by_value('Mars').click()
    time.sleep(3)
    
    # Now that splinter has us on the right page, we use beautiful soup to find and isolate the first mars image
    url = 'https://www.jpl.nasa.gov/images'
    html = browser.html
    
    # Create BeautifulSoup object; parse with 'html
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve the cover object for the first image - results are returned as an iterable list
    image = soup.find('div', class_='sm:object-cover object-cover')
    time.sleep(2)
    # scrape the first mars web link 
    featured_image_url = image.find("img")['data-src']
    time.sleep(3)
    
    # add our featured image to the mars dictionary
    mars_data["featured_image"] = featured_image_url
    
    #Quit Browswer
    browser.quit()
    
    # Mars Facts
    
    # URL of page to be scraped
    url='https://space-facts.com/mars'
    
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    
    #Pull the record detail from the table
    
    #Define the elements
    tr_elements = doc.xpath('//tr')
    
    #Create empty list
    col=[]
    i=0
    
    #For each row, store each first element (header) and an empty list
    for t in tr_elements[:9]:
        i+=1
        name=t.text_content()
        col.append((name))
        
    #Create Pandas DataFrame
    df=pd.DataFrame(col, columns = ["Trait"])
    df[['Trait','Measures']] = df['Trait'].str.split(':',expand=True)
    
    # Set Trait column as the indes
    df.set_index('Trait', inplace=True)
    
    #Convert dataframe to an html file
    mars_facts_html = df.to_html(classes="table table-striped table-bordered")
    
    # add our mars facts to the mars dictionary
    mars_data["mars_facts"] = mars_facts_html
    
    
    # Mars hemispheres
    
    #Use a Python dictionary to store the Mars Hemispheres data
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url":
     "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": 
     "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": 
     "https://astrogeology.usgs.gov/cache/images/55f04ff759b242bdff8833374544b1be_syrtis_major_unenhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": 
     "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"}
    ]
    
    # add our mars hemispherse images dictionary to the mars dictionary
    mars_data["mars_hemispheres"] = hemisphere_image_urls
    
    mars_data
    return mars_data
    
    

        
    


    
    
    
    
    
    
    
    
    
    
    
    
    