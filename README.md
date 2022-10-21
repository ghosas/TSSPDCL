# TSSPDCL
This python code is scrapping web and twitter to find out outage time in area. 
Source :
  Twitter : https://twitter.com/TsspdclCorporat
  Scheduled outage plan : https://webportal.tssouthernpower.com/TSSPDCL/Information/ScheduledOutageInformation.jsp![image](https://user-images.githubusercontent.com/38706502/197269467-760fe161-8b2b-4920-9f7d-8e87359df818.png)

Implementation 

Webscrapper
Use requests and beautifulsoup to parse webpage table and then store in Panda. Search table column "Area Affected" using Panda. 
