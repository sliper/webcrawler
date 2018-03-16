from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTittle(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return e
  try:
    bsObj = BeautifulSoup(html.read(), "html.parser")
    title = bsObj.body.h1
  except AtrributeError as e:
    return e
  return title
title = getTittle("http://www.pythonscraping.com/pages/page100.html")
print(title)
