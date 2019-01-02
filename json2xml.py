import json
import xmltodict
import re


try:   
   sys.argv[1]
except IndexError:  
   print("You must add the name of the json input file")
   sys.exit()

jsonFile = sys.argv[1]
 
with open(jsonFile, 'r') as f:
    jsonString = f.read()
f.close()

data = {}
data['item'] = json.loads(jsonString)
root = {}
root['root'] = data

'''
print('JSON input:')
print(jsonString)
'''

# remove spaces from keys name 
xmlString = xmltodict.unparse(json.loads((re.sub(r'\s(?=\w+":)',"_",str(json.dumps(root))))), full_document=False,pretty=True)
 
with open('output.xml', 'w') as f:
    f.write(xmlString)
    print('\nXML output(output.xml) created')
f.close()
