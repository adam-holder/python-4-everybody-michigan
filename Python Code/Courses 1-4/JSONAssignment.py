import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
runningSum = 0
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)

print ('User count:', len(info["comments"]))
#print (info)
#print (info["comments"])
print('Retrieving',url)
print('Retrieved', len(data), 'characters')
#print(json.dumps(info, indent=2))

for item in info["comments"]:
    itemCount = int(item["count"])
    #print('Name:', item["name"], 'Count:', itemCount)
    runningSum = runningSum + itemCount

print('Total sum of all counts:',runningSum)
