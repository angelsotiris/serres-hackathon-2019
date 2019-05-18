
class LogLine:
    def __init__(self, IP, date, requestType, requestPath, response):
        self.IP = IP
        self.date = date
        self.requestType = requestType
        self.requestPath = requestPath
        self.repsonse = response
    



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
                print(line + " heeeey errrorr")
                


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













