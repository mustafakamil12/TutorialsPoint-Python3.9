import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    #print("tree = ", tree)

    # get root element
    root = tree.getroot()
    #print("root = ", root)

    # create empty list for news items
    apikeys = []

    # iterate news items
    for item in root.findall('./email/apikey'):
        #print(f"item = {item}")
        #print(f"item.text = {item.text}")
        # empty news dictionary
        apikeys.append(item.text)

    return apikeys


# parse xml file
newsitems = parseXML('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/server_config.xml')

print(f"newsitems = {newsitems}")
