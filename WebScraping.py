#Will need to grab the request library
from bs4 import BeautifulSoup
import requests

#GET Request

#Scrape From Render Website
req = requests.get('https://python-web-7bsx.onrender.com')
soup = BeautifulSoup(req.text, "html.parser")


#Scraping HTML 
office_supplies = soup.findAll("span", attrs={"class":"text"})


#For Loop To Gather the Office Supplies From the HTML Page
for quote in office_supplies:
    print(office_supplies)

#Input
continueProgram = input("Pause Break. Type anything to see the rest of the results in html ")

#Gathers HTML Code
print(req)
print(req.content)
