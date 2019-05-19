
import json, urllib
import matplotlib.pyplot as plt
import time

class Date:
    def __init__(self,year,month,day,hours,minutes,seconds,UTC):
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes =  minutes
        self.seconds = seconds
        self.UTC = UTC
    


class LogLine:
    def __init__(self, IP, date, requestType, requestPath, response,size):
        self.IP = IP
        dateSplitted = date.split('/')
        day = dateSplitted[0]
        month = dateSplitted[1]
        rest = dateSplitted[2]
        restSplitted = rest.split(':')
        year = restSplitted[0]
        hours = restSplitted[1]
        minutes = restSplitted[2]
        restSplitted2 = restSplitted[3].split('+')
        
        seconds = restSplitted2[0]
        UTC = restSplitted2[1]
        self.Fdate = Date(year,month,day,hours,minutes,seconds,UTC)
        self.requestType = requestType
        self.requestPath = requestPath
        self.response = response
        self.size = size
        self.category = 1
    
        

###Methon which returns country for each IP
def findCountryViaIP(IPs,IPsAndCountries):
    start = time.time()
    for i in IPs:
        with urllib.request.urlopen('http://api.ipstack.com/'+i+'?access_key=844d3b30e00ba26f12ab92f62e33b2d3&format=1') as url:
            data = json.loads(url.read().decode())
            IPsAndCountries[i] = data['country_name']
    end = time.time()
    print('Time of findCountryViaIP\'s execution :' + str(end - start))    
        
#Classifier       
def ClassifyRequests(keyWords,logFile):
    for i in logFile:
        for keyWord in keyWords:
            word = str(keyWord).replace('\n','')
            if(word 
               in i.requestPath):
                i.category = 0
                break
            
def readKeyWords(filename):
    listWithKeyWords =[]
    with open(filename,'r') as file:
        for i in file.readlines():
            listWithKeyWords.append(i)
            
        file.close()
    return listWithKeyWords
def readFile(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        
        for line in lines:
            splitted  = line.split()
            try:
                UTC = splitted[4]
                UTC = UTC.replace(']','')
                del splitted[7],splitted[4],splitted[2],splitted[1]
                splitted[2] = splitted[2].replace('\"','')
                splitted[1] = splitted[1].replace('[','')
                fullDate =  splitted[1] + UTC
                IP, date, requestType,requestPath,response,size= splitted[0],fullDate,splitted[2],splitted[3],splitted[4],splitted[5]
                simpleLine = LogLine(IP,date,requestType,requestPath,response,size)
                logFile.append(simpleLine)
            except:
                print("")
        file.close()


              
###TASK1
def calculateTraffic(logFile):
    count = 0
    for i in logFile:
        if(i.requestType=='POST'):
            count += 1
        elif(i.requestType=='GET'):
            count += 1
    return count   

    
###TASK2
def requestsWith5xxErrors(logFile):
    count = 0
    for i in logFile:
        if(i.response[0]=='5'):
            count+=1     
    return count



   
###TASK3
def differentIPs(logFile):
    dictionary = {}
    for i in logFile:
        if(i.IP in dictionary.keys()):
            dictionary[i.IP] += 1
        else:
            dictionary[i.IP] = 1
            
    return dictionary

def serverAttacksPercentage(logFile):
    count = 0
    for i in logFile:
        if(i.response=='404'):
            count+=1     
    return count/len(logFile)

        
def requestsPerHour(logFile):
    hoursDict ={}
    for i in logFile:
        if(i.Fdate.hours in hoursDict.keys()):
            hoursDict[i.Fdate.hours] += 1
            
        else:
            hoursDict[i.Fdate.hours] = 1
            
    return hoursDict
        

def calculateRequestsPerCountry():
    rPerCountry = {}
    for i in IPsAndCountries:
        country = IPsAndCountries[i]
        count = dictionary[i]
        if(country in rPerCountry.keys()):
            rPerCountry[country] += count
        else:
            rPerCountry[country] = count
    return rPerCountry

def calculateAttacks(logFile):
    count = 0
    for i in logFile:
        if(i.category==0):
            count+=1
    return count



logFile = []



readFile('website-access.log.1')
readFile('website-access.log.2')
readFile('website-access.log.3')
readFile('website-access.log.4')
readFile('website-access.log.5')
readFile('website-access.log.6')
readFile('website-access.log.7')
readFile('website-access.log.8')
readFile('website-access.log.9')
readFile('website-access.log.10')
print('-----------------------------') 
##TASK1
print('------------TASK 1-----------') 
print("Count Of Traffic : " + str(calculateTraffic(logFile)))

###TASK2
print('------------TASK 2-----------') 
print("Count of 5xx Error's Responses : " + str(requestsWith5xxErrors(logFile)))


###TASK3
print('------------TASK 3-----------')
dictionary = differentIPs(logFile)
print("Count of different IPs : " + str(len(dictionary)))

###TASK 4
keyWords = readKeyWords('keywords.txt')
ClassifyRequests(keyWords,logFile)
countOfAttacks = calculateAttacks(logFile)
print('------------TASK 3-----------')
print("Count of attacks : " + str(countOfAttacks))
###Rest API 
###Send IP and returns Country
'''
IPsAndCountries = {}
findCountryViaIP(dictionary.keys(),IPsAndCountries)
'''
HoursDict = {}
HoursDict = requestsPerHour(logFile)


D = {u'Label1':26, u'Label2': 17, u'Label3':30}
###PLOTs
plt.plot(HoursDict.keys(),HoursDict.values())
plt.axis([0,23,min(HoursDict.values()),max(HoursDict.values())])
plt.xticks(range(len(HoursDict)), list(HoursDict.keys()))
plt.ylabel('Attacks per time')
plt.xlabel('Hours of the day')
plt.show()

'''
RequestsPerCountry = calculateRequestsPerCountry()

figureObject, axesObject = plt.subplots()
axesObject.pie(RequestsPerCountry.values(),labels=RequestsPerCountry.keys())
axesObject.axis('equal')
plt.show()

'''










