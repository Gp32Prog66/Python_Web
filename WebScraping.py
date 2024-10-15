#Will need to grab the request library
from bs4 import BeautifulSoup
import requests

#GET Request
req = requests.get('https://python-web-7bsx.onrender.com')
soup = BeautifulSoup(req.text, "html.parser")


office_supplies = soup.findAll("span", attrs={"class":"text"})


#For Loop To Gather the Quote and the Author of the Quote
for quote in office_supplies:
    print(office_supplies.text)

#Input
continueProgram = input("Pause Break. Type anything to see the rest of the results in html ")

#Gathers HTML Code
print(req)
print(req.content)
