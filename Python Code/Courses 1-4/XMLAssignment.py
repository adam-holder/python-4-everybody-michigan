import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
runningSum = 0
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
commentList = tree.findall('comments/comment')
print('Retrieving',url)
print('Retrieved', len(data), 'characters')
print ('User count:', len(commentList))
for item in commentList:
    #print ('count', item.find('count').text)
    itemCount = int(item.find('count').text)
    runningSum = runningSum + itemCount
    #print ('The current running Sum is', runningSum)
print('Total sum of all counts:',runningSum)
