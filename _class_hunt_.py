import requests,os
import re
import http.cookies
from bs4 import BeautifulSoup


class requt:

    def __init__(self,urlsa:str = None) -> None:
        self.urlsa  = urlsa
        self.sesion = requests.Session()
        self.repspo = self.sesion.get(self.urlsa)        
        pass

    def squareup(self):
        try:
            lol = self.repspo.headers['Set-Cookie']
            cookies = http.cookies.SimpleCookie()
            cookies.load(lol)
            domain = cookies["squareGeo"]["domain"]
            if 'squareup.com' == domain:return True
            else: return False
        except: return None 
    
    def clou(self):
        try:
            if self.repspo.headers: return self.repspo.headers['Server']
            else : return False
        except: return False
    def Shopify(self):
        try:
            if  "Shopify" == self.repspo.headers['powered-by'] : return 'Shopify'
            else : return False
        except :
            return False
                
    def stripe(self):
        resultado = re.search(r'"default_gateway"\s*:\s*"([^"]+)"', self.repspo.text)
        if resultado:
            stripet = resultado.group(1)
            if 'stripe' == stripet : return True
            elif stripet: return stripet
            else : False
        else: return False
    
    def postData(self):
        return self.repspo.headers


class GoogleQuey:
    def __init__(self,query:str = None) -> None:
        self.query    = query
        self.sesion   = requests.Session()
        self.url      = f"https://www.google.com/search?q={self.query}&start=10&sourceid=chrome&ie=UTF-8"
        self.response = self.sesion.get(self.url)
        pass

    def getbs4(self):
        responBs = BeautifulSoup(self.response.text, 'html.parser').find_all('a', href = True)
        return responBs
    
