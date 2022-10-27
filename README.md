# TSSPDCL
This python code is scrapping web and twitter to find out outage time in area. 
Source :
  Twitter : https://twitter.com/TsspdclCorporat
  Scheduled outage plan : https://webportal.tssouthernpower.com/TSSPDCL/Information/ScheduledOutageInformation.jsp
  
  
Implementation 

Webscrapper
Use requests and beautifulsoup to parse webpage table and then store in Panda. Search table column "Area Affected" using Panda. 
