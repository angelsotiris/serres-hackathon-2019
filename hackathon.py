import time

    
    
    
    
    
    
    
    
    
    
    
    
def countofIPs(filename):
    c = 0;
    with open(filename,"r") as file:
        lines = file.readlines()
        
        for line in lines:
                lineSplitted = line.split('-')
                ##remove the space
                ##print(lineSplitted)
                if(' ' in lineSplitted):
                    lineSplitted.remove(' ')
                lineToList = list(lineSplitted)
                try:    
                        dictionary[lineToList[0]] = lineToList[1]
                        
                except:
                    print(c)
                c +=1
        
        file.close()
        

start = time.time()
    

dictionary = {}
countofIPs('website-access.log.1')
print('1 file checked')
countofIPs('website-access.log.2')
print('2 file checked')
countofIPs('website-access.log.3')
print('3 file checked')
countofIPs('website-access.log.4')
print('4 file checked')
countofIPs('website-access.log.5')
print('5 file checked')
countofIPs('website-access.log.6')
print('6 file checked')
countofIPs('website-access.log.7')
print('7 file checked')
countofIPs('website-access.log.8')
print('8 file checked')
countofIPs('website-access.log.9')
print('9 file checked')
countofIPs('website-access.log.10')
print('10 file checked')
end = time.time()
print(end - start)