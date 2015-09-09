#!/usr/bin/python
 
import urllib
from threading import Thread
import re
from Queue import Queue
 
NUM_WORKERS = 10
 
class Dnld:
  def __init__(self):
    self.Q = Queue()
    for i in xrange(NUM_WORKERS):
      t = Thread(target=self.worker)
      t.setDaemon(True)
      t.start()
 
  def worker(self):
    while True:
      url, localFile = self.Q.get()
      try:
        print ("downloading %s to %s" % (url,localFile))  
        urllib.urlretrieve(url,localFile)    
      except Exception, e:
        Q.put(('error', url, e))
        try: f.close() # clean up
        except: pass
  def download(self, url,localFile):
    self.Q.put((url, localFile))
 
class VariantDownloader(object):
  def __init__(self,downloader,baseUrl):
    print ('> create variant %s' % baseUrl)
    self.chunksUrl=set()
    self.baseUrl=baseUrl
    self.downloader=downloader
    self.reg=re.compile('^(.*ts)[\n\r]*$')
  def refresh(self):
    print ("refresh %s" % self.baseUrl)
#    print (repr(self.chunksUrl))
    f = urllib.urlopen(self.baseUrl)
    data = f.readlines()
    f.close()
    chunks=[]
    for a in data:
      res=self.reg.match(a)
      if res:
        chunks.append(res.group(1))
    for a in set(chunks) - set(self.chunksUrl):
      url=appendUrl(self.baseUrl,a)
      print ('adding chunk %s' % url)
      self.downloader.download(url,'./'+a)
      self.chunksUrl|=set([a])
   
 
class AdassDownloader(object):
  def __init__ (self):
    self.downloader=Dnld()
    self.variants=[]
    self.reg=re.compile('^(.*m3u8)[\n\r]*$')
  def setRoot(self,xUrl):
    print ('> downloading root %s' % xUrl)
    f = urllib.urlopen(xUrl)
    data = f.readlines()
    print (data)
    f.close()
    variant = filter (self.reg.match,data)
    print (variant)
    for a in variant:
      self.variants.append(VariantDownloader(self.downloader,appendUrl(xUrl,a)))
  def go(self):
    while(True):
      for a in self.variants:
        a.refresh()      
 
def appendUrl(base,end):
  newBase='/'.join (base.split('/')[:-1])
#  print (base,end,newBase)
  return newBase+'/'+end  
 
a=AdassDownloader()
a.setRoot('http://multimedioshls-i.akamaihd.net/hls/live/223119/57828478001-2/master/720/index.m3u8')
a.go()