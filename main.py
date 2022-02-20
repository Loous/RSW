from bs4 import BeautifulSoup
import requests
import sys
import os.path
import os
from ping3 import ping

from transformurl import trnurl
import crtdirec

class Mrcr:
    """
    It search sublinks in a URL and after save that links in a file with its URL name associated
    
    WARNING: a problem with single page aplication, if you put a URL of a single page aplication
    is posible that it no work
    """
    
    
    def __init__(self):
    
        self._parameters = sys.argv
        self._url = ""
        
        
    def reqUrlss(self):
        
        if len(self._parameters) == 2:
            url = self._parameters[1]
            x = ping(trnurl(url))
            
            if x is not False:
                
                self._url = url
                req = ""
                
                try:
                    
                    req = requests.get(url).text
                    
                except requests.exceptions.MissingSchema:
                    print("The URL isn't valid")
                    
                if req != "":
                    
                    soup = BeautifulSoup(req, "html.parser")
                    links = soup.find_all("a")
                    
                    if len(links) == 0:
                        print("None links were found")
                        
                    else:
                        self.saveLinks(links)
                        
            else:
                print("The URL must be like this https://example.com")
            
        else:
            print("you must put a URL to search sublinks")
             
                
    def saveLinks(self, links): # We save the links finded in the URL in a file
        
        def rwfile(type):
        
            with open("links.txt", type) as archivo:
                for n in links:
                    if "https" not in n["href"]:
                        continue
                    
                    else:
                        archivo.writelines(f'{n["href"]}\n')
                        
        if os.path.exists("links.txt") is False:
            rwfile("a")
            
        else:
            rwfile("w")
            
        self.linksRead()
            
            
    def linksRead(self): # We save the URL name and the url associated
        
        data = {}
        
        with open("links.txt", "r") as archivo:
            for n in archivo.readlines():
                n = n.strip()
                if n[-1] == "/":
                    x = n.split("/")[-2]
                    data[x] = n
                    
                    
                else:
                    x = n.split("/")[-1]
                    data[x] = n
                    
        self.createUrFiles(data)
        
        
    def getUrls(self, url): # We get all links of the URL that they have the scheme https
        
        req = requests.get(url).text
        soup = BeautifulSoup(req, "html.parser")
        links = soup.find_all("a")
        
        lista = []
        
        for n in links:
            
            try:
            
                if "https" not in n["href"]:
                    continue
                
                else:
                    lista.append(n["href"])
                    
            except KeyError:
                continue
                
        return lista
                    
                    
    def createUrFiles(self, data): # We create a txt file with its respective links
        
        k = crtdirec.directoryName(self._url)
        crtdirec.createDirectory(k)
        
        def crfl(nameUrl, type, dataa):
            
            if os.path.exists(os.path.join(os.getcwd(), k, f"{nameUrl}.txt")):
                return False
            
            else:
                with open(f"{nameUrl}.txt", type) as archivo:
                    for n in dataa:
                        archivo.writelines(f"{n}\n")
                        
                crtdirec.moveFiles(f"{nameUrl}.txt", k)
                        
        
        for urlName, url in data.items():
            x = self.getUrls(url)
            
            try:
            
                crfl(urlName, "a", x)
                
            except OSError: # Some URL names will be ignored because the URL name is very long
                continue
            
        print("The files has been created successfully!")
            
            
if __name__ == "__main__":
    Mrcr().reqUrlss()
            
            
   
                
        
        
        
        
        
                
                        
               
                
            
            
            
             
                        
        
                
            
        
        
            
            
            
            
            
            

            
            
            
            
            
            
            


























































































