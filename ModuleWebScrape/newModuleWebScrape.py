from urllib.request import urlopen as urequest
from bs4 import BeautifulSoup as soup

modulePage = 'http://www.open.ac.uk/courses/modules'
OU = "http://www.open.ac.uk"

#grabbing OU module page
uClient = urequest(modulePage)

#Making it readable
pageHtml = uClient.read()

#closing connection
uClient.close()

# structure the page into hmtl
pageSoup = soup(pageHtml, "html.parser")

#print(pageSoup.h1)

#modules are located in class "int-grid7" on the page
modules = pageSoup.findAll("div",{"class":"int-grid7"})

for module in modules:
    print(module.text)

#level are located in class "int-grid5" on the page
levels = pageSoup.findAll("div",{"class":"int-grid5"})

for level in levels:
    print(level.text)

# to get credits these are on another page, so will need to access each page and grab the data
modules = pageSoup.findAll("div",{"class":"int-grid7"})

for module in modules:
    for links in module:
        topUpLink = str(links.get("href"))
        #print(OU+topUpLink)
        client = urequest(OU+topUpLink)
        webPage = client.read()
        client.close()
        souped = soup(webPage,"html.parser")
        credits = souped.find(text="Credits").findNext('dd')
        print(credits.text)
