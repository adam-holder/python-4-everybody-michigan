import xml.etree.ElementTree as ET
#ET is an alias for xml.etree.ElementTree
#''' encompasses a much larger group of data
#This spawns an element tree
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
#this finds the text that is under the name tag
#tree.find looks at an element tree
#this will find "Chuck"
print('Name:',tree.find('name').text)
#go find me the attribute 'hide' in the email tag
print('Attr:',tree.find('email').get('hide'))


#--------------------------------------------------------------------


import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

#stuff here is a tree object
stuff = ET.fromstring(input)
#find all of the user tags under "users"
#creates a list of tags
lst = stuff.findall('users/user')
print ('User count:', len(lst))
for item in lst:
    print ('Name', item.find('name').text)
    print ('Id', item.find('id').text)
    print('Attribute', item.get("x"))
