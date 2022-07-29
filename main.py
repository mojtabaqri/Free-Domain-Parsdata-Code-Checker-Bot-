import asyncio
import re
import ghasedakpack
import urllib.request
from bs4 import BeautifulSoup




def readPage(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    HtmlString = mybytes.decode("utf8")
    fp.close() 
    return HtmlString



def parsHtml():# Get Code From ParsData 
    soup = BeautifulSoup(readPage("https://www.parsdata.com/Default.aspx?ajax=1&sys=data&out=FDAjax&cul=fa-IR"), 'html.parser')
    el = soup.find_all("div", {"class": "fdCode"})
    result = []
    for th in el:
        result.extend(th.find_all('span'))
    code=result[0].text   
    





# sms = ghasedakpack.Ghasedak("2cb971f525dda65a268fefb25ba37afc14f90c4c3cc1b9c9629836c0833328cc")
