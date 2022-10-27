import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webportal.tssouthernpower.com/TSSPDCL/Information/ScheduledOutageInformation.jsp"

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

# Find out headers and position
head = {}
header = soup.find_all('td',attrs={'bgcolor': '#083557'})
# print(header)
for item in header:
    record = item.find('b')
    pos = header.index(item)
    rec= record.get_text()
    head[rec]=pos
# print(head)

#Creating Dataframe
df =pd.DataFrame(columns=head.keys())
# print(df)


#Find out columns 
table = soup.find_all('tr',attrs={'bgcolor':['#e6f4fe','#FFFFFF']})
for element in table :
    # print(type(element))
    # print(element)
    cols = element.find_all('td')
    li = []
    for data in cols:
        d = data.get_text()
        li.append(d)
    # print(li)
    df.loc[len(df)] = li
    # print("=======================================")

# print(df)
# print(df.loc[df['Area Affected']=='Kendriya Vihar'])
print(df.loc[df['Area Affected']=='VEPOOR'])

