import urllib2
from bs4 import BeautifulSoup
import json
# Code to handle proxy
proxy = urllib2.ProxyHandler({'http': 'http://HITN028:483412294@172.31.1.6:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

def ExpectedDelay(TrainNo):
    page=urllib2.urlopen('http://runningstatus.in/history/'+str(TrainNo)+'/weekly').read()
    soup = BeautifulSoup(page, 'html.parser')
    rows = [row for row in soup.find("table").find_all("tr")]
    size = len(rows)-1
    delays = [rows[i].find_all("td")[2] for i in range(1,size)]
    delays = [delay.contents[0] for delay in delays]
    avgdelay=0;
    for delay in delays:
        if delay[0] == '-':
            pass
        elif delay[3] == 'M':
            avgdelay=avgdelay+int(delay[0:2])
        else:
            avgdelay=avgdelay+int(delay[0:2])*60+int(delay[7:9])
    if len(delays)==0:
        return -1
    return avgdelay/len(delays)

source='ndls'
destination='ald'
date='27-08' #dd-mm
apikey='iizgz6230'

url='http://api.railwayapi.com/between/source/'+source+'/dest/'+destination+'/date/'+date+'/apikey/'+apikey+'/'

datas = urllib2.urlopen(url).read()
datas=json.loads(datas)
#print data


import sqlite3 as sq3
conn=sq3.connect('delay.db')
c=conn.cursor()
c.execute('''DROP TABLE IF EXISTS "delay";''')
c.execute('''CREATE TABLE delay (TrainNO int pmary key,delay int,name char(20))''')

trains=[]
#i=5
for data in datas['train']:
    train={}
    name=train['name']=data['name']
    no=train['no']=data['number']
    delay=train['delay']=ExpectedDelay(train['no'])
    trains.append(train)
    c.execute("INSERT INTO delay VALUES(?, ?, ?)",(no,delay,name))
    print train
    # i=i-1
    # if(i<0):
    #     break
conn.commit()
for row in c.execute('select name,delay from delay'):
    print row
print trains