from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
url="https://www.medtalks.in/live-corona-counter-india"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')

bsobj=BeautifulSoup(webpage, 'html.parser')
k=bsobj.findAll("tbody")[0]
r=k.findAll("tr")
for i in r[0:19]:
    print(i.text.split("\n")[1])
print("------------------------------------------\n")    
for j in r[0:19]:
  print(j.text.split("\n")[2])
print("------------------------------------------\n")  
#for l in r:
 #   print(l.text.split("\n")[5])

#for b in bsobj.findAll("button",{"class":"btn btn-light date-btn"}):
#print(b['data-date'])

