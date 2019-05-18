
class LogLine:
    def __init__(self, IP, date, requestType, requestPath, response):
        self.IP = IP
        self.date = date
        self.requestType = requestType
        self.requestPath = requestPath
        self.response = response
    



def readFile(filename):
    with open(filename,'r') as file:
        lines = file.readlines()
        
        for line in lines:
            splitted  = line.split()
            try:
                del splitted[9],splitted[7],splitted[4],splitted[2],splitted[1]
                splitted[2] = splitted[2].replace('\"','')
                splitted[1] = splitted[1].replace('[','')
                IP, date, requestType,requestPath,response = splitted[0],splitted[1],splitted[2],splitted[3],splitted[4]
                simpleLine = LogLine(IP,date,requestType,requestPath,response)
                logFile.append(simpleLine)
            except:
                print("heeeey errrorr")
                
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

##TASK1
print("Count Of Traffic : " + str(calculateTraffic(logFile)))

###TASK2
print("Count of 5xx Error's Responses : " + str(requestsWith5xxErrors(logFile)))









