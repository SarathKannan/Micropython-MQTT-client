import ujson
import machine

def extract_content(mainContent):
    sub1 = "ssid="
    sub2 = "&password="
    sub3 = "&ip="
    sub4 = "&port="
    sub5 = " HTTP"
    
    idx1 = mainContent.index(sub1)
    idx2 = mainContent.index(sub2)
    idx3 = mainContent.index(sub3)
    idx4 = mainContent.index(sub4)
    idx5 = mainContent.index(sub5)
    
    ssid = mainContent[idx1 + len(sub1) : idx2]
    password = mainContent[idx2 + len(sub2) : idx3]
    ip = mainContent[idx3 + len(sub3) : idx4]
    port = mainContent[idx4 + len(sub4) : idx5]
        
    print('ssid = %s' % ssid)
    print('password = %s' % password)
    print('ip = %s' % ip)
    print('port = %s' % port)
    
    
    jsonData = {'ssid': ssid, 'password': password, 'ip': ip, 'port': port, 'isConfigFound': True}
    jsonObj = ujson.dumps(jsonData)
    
    createFile = open('config.json', 'w')
    createFile.write(jsonObj)
    createFile.close()
    machine.reset()

    
    